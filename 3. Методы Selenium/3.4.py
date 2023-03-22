# Откройте сайт с помощью Selenium;
# На сайте есть определённое количество секретных cookie;
# Ваша задача получить все значения и суммировать их;
# Полученный результат вставить в поле для ответа.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://parsinger.ru/methods/3/index.html")
    cookies = browser.get_cookies()
    sum_of_value = 0
    for cookie in cookies:
        sum_of_value += int(cookie['value'])

    print(sum_of_value)
finally:
    time.sleep(2)
    browser.close()
    browser.quit()