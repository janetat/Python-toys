import requests
from bs4 import BeautifulSoup

# cookies中存了sessionID和其他信息，来验证身份和提供信息给服务器
# 存取cookies，因为登录页面和登录后的页面的cookies不同，所以如果登录成功后还是用登录前的cookies的话，操作会失败，返回到登录页面。
# 用update整合登录前后的cookies，因为可能有关联。
cookie_dict = {}

# 1. 获取authenticity_token，或者又叫csrf_token，防止表单重复提交，防止csrf攻击。其实就是token的功能。
# 发送http请求，获取登录页面
response1 = requests.get('https://github.com/login')
# 实例化文档解析器bs
s1 = BeautifulSoup(response1.text,'html.parser')
# 通过bs找到对应的标签对象，再找到token的值
token = s1.find(name='input',attrs={'name':'authenticity_token'}).get('value')
# 获取第一次请求（登录页面）的cookies，以字典的形式。因为requests的接口是要求传入的cookies是字典形式的。
cookie_dict.update(response1.cookies.get_dict())

# 2. 将用户名，密码和token，登录页面的cookies发送到服务端，post请求进行登录操作。
"""
utf8:✓
authenticity_token:ollV+avLm6Fh3ZevegPO7gOH7xUzEBL0NWdA1aOQ1IO3YQspjOHbfnaXJOtVLQ95BtW9GZlaCIYd5M6v7FGUKg==
login:asdf
password:asdf
commit:Sign in
"""
# 把'login'和'password'字段替换为自己的账号和密码
response2 = requests.post(
    'https://github.com/session',
    data={
        "utf8": '✓',
        "authenticity_token": token,
        'login': 'xxx@qq.com',
        'password': 'xxx',
        'commit': 'Sign in'
    },
    cookies=cookie_dict
)
# print(response2.text)

# 3. 登录成功后，利用登录后的cookies。进行访问/settings/emails这个页面的操作
cookie_dict.update(response2.cookies.get_dict())
#
response3 = requests.get(
    url='https://github.com/settings/emails',
    cookies=cookie_dict
)
print(response3.text)

# 4. 操作成功后，将返回的页面写入文件中。（可以本地live server浏览）
with open('./test1111111.html','wb') as f:
        f.write(response3.content)
