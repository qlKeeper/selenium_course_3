# Откройте сайт с помощью Selenium;
# При обновлении сайта, в id="result" появится число;
# Обновить страницу возможно придется много раз, т.к. число появляется не часто;
# Вставьте полученный результат в поле для ответа:

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://parsinger.ru/methods/1/index.html")
        
    while not (browser.find_element(By.ID, "result").text.isdigit()):
        browser.refresh()
    print(browser.find_element(By.ID, "result").text)
    
finally:
    browser.close()
    browser.quit()