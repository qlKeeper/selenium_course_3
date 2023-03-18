# Открываем сайт при помощи selenium;
# Применяем метод By.PARTIAL_LINK_TEXT или By.LINK_TEXT;
# Кликаем по ссылке с текстом 16243162441624;
# Результат будет ждать вас в теге <p id="result"></p>  ;
# Скопируйте найденный результат в поле ниже.


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/2/2.html")
    browser.find_element(By.LINK_TEXT, "16243162441624").click()
    time.sleep(10)