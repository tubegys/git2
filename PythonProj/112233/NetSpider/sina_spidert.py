import requests
from bs4 import BeautifulSoup
res = requests.get('http://www.sina.com.cn/')
res.encoding = "utf-8"
soup = BeautifulSoup(res.text, 'html.parser')
for news in soup.select('a'):
    print(news.text)














