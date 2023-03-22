# Откройте сайт с помощью Selenium;
# Ваша задача получить все значения cookie с чётным или кратным 10 числа после 
# "_" и суммировать их;
# Полученный результат вставить в поле для ответа.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/methods/3/index.html")
    cookies = browser.get_cookies()
    sum_of_value = 0
    for cookie in cookies:
        name_num = int(str(cookie['name']).replace("secret_cookie_", ''))
        if (name_num % 2 == 0) or (name_num % 10 == 0):
            sum_of_value += int(cookie['value'])
        
    print(sum_of_value)