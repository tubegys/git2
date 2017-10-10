
import urllib.request as ur
url = 'http://www.baidu.com'
reponse = ur.urlopen(url)
print(reponse.getcode())
