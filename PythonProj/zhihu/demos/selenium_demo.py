from selenium import webdriver
import time
import requests

browser = webdriver.Chrome(executable_path='D:\chromedriver.exe')
browser.implicitly_wait(10)
browser.get('https://www.zhihu.com/#signin')
# print(browser.page_source)
browser.find_element_by_css_selector('.view-signin input[name="account"]').send_keys('17701683279')
browser.find_element_by_css_selector('.view-signin input[name="password"]').send_keys('coekie')
time.sleep(10)
cookies = browser.get_cookies()
print(cookies)
print(browser.current_url)


# def get_logined_url(account, password):
#     browser = webdriver.Chrome(executable_path='D:\chromedriver.exe')
#     browser.implicitly_wait(10)
#     browser.get('https://www.zhihu.com/#signin')
#     browser.find_element_by_css_selector('.view-signin input[name="account"]').send_keys(account)
#     browser.find_element_by_css_selector('.view-signin input[name="password"]').send_keys(password)
#     time.sleep(10)  # 给人识别验证码所等待的时间
#     print(browser.current_url)
#     cookies = browser.get_cookies()
#     print(cookies)
#     return browser.current_url
#
# browser = webdriver.Chrome(executable_path='D:\chromedriver.exe')
# print('END')