import urllib.request as ur, re
import urllib

def get_html(url):
    page = ur.urlopen(url)
    html = page.read()
    html = html.decode('utf-8')
    return html


def get_img(html):
    reg = re.compile(r'src="(.+?\.png)"')
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg' % x)
        x +=1



html = get_html('http://www.baidu.com')
print(html)
get_img(html)
