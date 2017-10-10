import urllib.request as ur
# urllib是python连接网页的模块,urllib是包，request是他的一个模块
url = ''
reponse = ur.urlopen(url, data)
