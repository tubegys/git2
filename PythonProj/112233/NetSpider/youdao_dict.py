import urllib.request as ur
request = ur.urlopen('http://www.baidu.com')
print(request)
html = request.read()
html = html.decode('utf-8')
print(html)