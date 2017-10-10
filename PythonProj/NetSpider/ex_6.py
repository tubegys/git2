import requests
from bs4 import BeautifulSoup
res = requests.get('http://www.sina.com.cn/')
res.encoding = "utf-8"
# print(res.text)
html_sample = """
<html>
    <body>
    <h1 id='title'>Hello World</h1>
    <a href='#' class='link'>This is Link1</a>
    <a href='# link2' class='link'>This is Link2</a>
    <body>
</html>
"""
soup = BeautifulSoup(html_sample, 'html.parser')
# print(type(soup))
header = soup.select('h1')  # 找h1标签，以列表的形式返回
print(header[0].text)  # 取标题

print('_________________________________________')

alink = soup.select('a')  # 找a标签，也以列表形式返回
for link in alink:
    print(link)
    print(link['href'])  # alink是列表,link可以理解为字典

print('_________________________________________')

class_link = soup.select('.link')  # 找到CSS样式叫link的样式
for clink in class_link:
    print(clink.text)

print('_________________________________________')

id_title = soup.select('#title')  # 找id为title的属性的标签
for it in id_title:
    print(it.text)
