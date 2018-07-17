# -*- coding: utf-8 -*-

'''
    @mission: 抓取知乎的exlore板块, 获取热门问题(10个)和对应的URL, 并存入文本里
    @tools: 1.requests抓取页面 2.PyQuery解析页面
'''
import requests
from pyquery import PyQuery as pq

base_url = 'https://www.zhihu.com'

# 要抓取的页面的URL
url = 'https://www.zhihu.com' + '/explore'

# 添加头部, 防止目标页面禁止访问、抓取
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}

# 抓取网页文本
html = requests.get(url, headers=headers).text

# 生成PyQuery对象, 以运用PyQuery提供的API解析页面
doc = pq(html)

# divs是生成器, 包含问题的区域
divs = doc('div.explore-feed.feed-item').items()

index = 1

# div是pyquery.pyquery.PyQuery对象, 所以div可以用PyQuery的API操作节点
for div in divs:
    question_node = div.find('a.question_link')
    question_text = question_node.text()
    question_link = base_url + question_node.attr('href')

    print(str(index) + '. ' + question_text)
    print(question_link)
    print('=' * 50)
    index += 1

    # answer = pq(div.find('textarea.content').html()).text()
    with open('./explore.txt', 'a', encoding='utf-8') as f:
        f.write('\n'.join([question_text, question_link]))
        f.write('\n' + '=' * 50 + '\n')
