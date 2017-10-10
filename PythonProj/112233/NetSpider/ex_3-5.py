from urllib import request, parse
req = request.Request('http://www.baidu.com')  # 加入协议头, 模仿浏览器浏览网页
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.9.3.1000 Chrome/39.0.2146.0 Safari/537.36')
resp = request.urlopen(req)
print(resp)
print(help(request.urlopen))

print('________________________________________________________________________________')
