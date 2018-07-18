# -*- coding: utf-8 -*-

'''
    @mission: 抓取新浪新闻中心每周点击量排行榜，并存入excel中
    @tools: 1.requests抓取页面 2.PyQuery解析页面 3.re过滤返回的数据 4.json将JSON字符串转换为dict 5.openpyxl保存到excel
'''
import requests
from pyquery import PyQuery
import re
import json
from openpyxl import Workbook

base_url = 'http://news.sina.com.cn/hotnews/index_weekly.shtml'

# # 要抓取的页面的URL
# url = 'https://www.zhihu.com' + '/explore'

# 添加头部, 防止目标页面禁止访问、抓取
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}

# 抓取网页文本
html = requests.get(base_url, headers=headers).content.decode('utf-8')

# 将返回的html页面封装成PyQuery对象, 以运用PyQuery提供的API解析页面
pyquery_doc = PyQuery(html)

pyquery_node_where_api = pyquery_doc('div.Cons#Con11 script')
# 得到了获取数据的API
data_url = pyquery_node_where_api.attr('src')

# 获取的数据是JS对象，里面有很多段JSON。另外，返回的是Unicode编码且链接中有多余的\, 要Unicode -> str, 去除多余的\
raw_data = requests.get(data_url).content.decode('unicode_escape')
raw_data = raw_data.replace('\\', '')

# print(raw_data)

# 用正则表达式抽取每段新闻的JSON。re.findall返回的是列表, 列表中存有每段的新闻的JSON。
data_list = re.findall(r'({.*?})', raw_data)


# Workbook is the container for all other parts of the document. (excel)
wb = Workbook()

# grab the active worksheet
ws = wb.active
ws.append(('序号', '标题', '媒体', '点击量', '时间', '链接'))


for index in range(1, len(data_list)):
    # 将JSON转换为Python字典对象, data_list的第一条不是新闻JSON
    cur_news = json.loads(data_list[index])
    title = cur_news.get('title')
    media = cur_news.get('media')
    click_num = cur_news.get('top_num')
    time = '{date} - {time}'.format(date=cur_news.get('create_date'), time=cur_news.get('create_time'))
    url = cur_news.get('url')
    # 将所要的信息放在当前worksheet的最低行
    ws.append((index, title, media, click_num, time, url))

# 保存到excel文件中
wb.save('sample.xlsx')


