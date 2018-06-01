import requests
from bs4 import BeautifulSoup

# 1. 发送http到要爬的网站，返回reponse
response = requests.get('http://www.autohome.com.cn/news/')
# 2. 设置返回的编码类型，默认为utf-8
response.encoding = 'gbk'
# 3. reponse.text返回html文本，content返回字节
html = response.text
# 4. 实例化BS解析器
soup = BeautifulSoup(html, 'html.parser')

# 5. 锁定区域
li_list = soup.find(id='auto-channel-lazyload-article').find_all(name='li')

for li in li_list:
    # 6. 标题
    title = li.find('h3') 
    if not title:
        continue
    # 7. 总结
    summary = li.find('p').text

    # 8. 文章链接
    # li.find('a').attrs['href'],字典
    # url = li.find('a').get('href')，和下一句实现相同的功能
    url_passage = 'https:' + li.find('a').attrs['href']

    # 9. 图片链接
    # img : //www3.autoimg.cn/newsdfs/g1/M06/93/3F/120x90_0_autohomecar__wKgHFVsNQEiAFTVzAAFgUvogiCc438.jpg
    # 要在前面加'https:'生成完整链接
    url_img = 'https:' + li.find('img').get('src')

    # 10. 打印相关信息
    print('标题：', title.text)
    print('简介：', summary)
    print('文章链接：', url_passage)
    print('图片链接：', url_img)
    print('-----------')

    # 11. 下载图片到指定目录
    pic = requests.get(url_img)
    file_name = "%s.jpg" % (title.text.replace('/', ''))
    with open('/home/allin/Desktop/picccc/' + file_name,'wb') as f:
        f.write(pic.content)



