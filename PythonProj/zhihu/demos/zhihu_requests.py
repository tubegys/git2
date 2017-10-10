import requests
import re
# from zheye import zheye
# z = zheye()
# positions = z.Recognize('E:\captcha.gif')
# print(positions)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko)"
                  " Chrome/59.0.3071.104 Safari/537.36",
    "Host": "www.zhihu.com",
    "Referer": "https://www/zhihu.com"
}
session = requests.session()


def get_xsrf():
    response = session.get("https://www.zhihu.com", headers=headers)
    # match_obj = re.match('.*name="_xsrf" value="(.*?)"', response.text, )
    match_obj = re.match('.*name="_xsrf" value="(.*?)"', response.text, re.DOTALL)
    if match_obj:
        return match_obj.group(1)
    else:
        return ""


def zhihu_login(account, password):

    post_phone_url = "https://www.zhihu.com/login/phone_num"
    post_data = {
        "_xsrf": get_xsrf(),
        "phone_num": account,
        "password": password,
        "captcha_type": "cn"
    }
    # 手机号登录
    if re.match("1\d{10}", account):
        session.post(post_phone_url, data=post_data, headers=headers)


def check_login():
    response = session.post("https://www.zhihu.com", headers=headers)
    with open('e:\index.html', 'wb') as f:
        f.write(response.text.encode('utf-8'))
    print(response.text, response.status_code)

zhihu_login('17701683279', 'coekie')
check_login()