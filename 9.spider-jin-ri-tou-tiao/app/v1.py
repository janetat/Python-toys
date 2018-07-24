'''
    __note__:今日头条的搜索是通过AJAX加载，再渲染页面。从chrome debugger查看XHR，分析链接。访问链接返回的是JSON格式。不用解析库，直接用reuqests转成json格式即可。
'''


import os
import requests
from urllib.parse import urlencode
from hashlib import md5
from multiprocessing.pool import Pool

GROUP_START = 1
GROUP_END = 5


def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '汽车',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # 直接转成json, type(response.json())是dict
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    data = json.get('data')
    if data:
        for item in data:
            # print(item)
            image_list = item.get('image_list')
            title = item.get('title')
            # print(image_list)
            if image_list:
                for image in image_list:
                    yield {
                        'image': image.get('url'),
                        'title': title
                    }


def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        local_image_url = item.get('image')
        new_image_url = local_image_url.replace('list','large')
        response = requests.get('http:' + new_image_url)
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb')as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to save image')


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


if __name__ == '__main__':
    # 开8个进程下载
    pool = Pool(processes=8)
    # 用列表表达式计算分组，得出的offset的列表。观察得offset=20代表第一页，offset=40代表第二页
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()