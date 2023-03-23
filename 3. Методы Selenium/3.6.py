# Откройте сайт с помощью Selenium;
# На сайте есть 42 ссылки, у каждого сайта по ссылке есть cookie с определёнными сроком жизни;
# Цель: написать скрипт, который сможет найти среди всех ссылок страницу с самым 
# длинным сроком жизни cookie и получить с этой страницы число;
# Вставить число в поле для ответа.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/methods/5/index.html")
    urls = browser.find_elements(By.CLASS_NAME, "urls")
    time.sleep(1)
    max_expiry, val = 0, 0
    
    for url in urls:
        url.click()
        time.sleep(0.1)
        cookies = browser.get_cookies()
        if max_expiry < int(cookies[0]['expiry']):
            max_expiry = int(cookies[0]['expiry'])
            val = browser.find_element(By.ID, 'result').text
        browser.back()
    
    print(val)
    time.sleep(1)

