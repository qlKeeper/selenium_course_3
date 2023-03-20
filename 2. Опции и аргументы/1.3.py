# Перенос профиля с основного браузера Chrome в браузер под управлением Selenium

import time
from selenium import webdriver

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('user-data-dir=C:\\Users\\user\\AppData\\Local\
\\Google\\Chrome\\User Data')
with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)
    time.sleep(10)
