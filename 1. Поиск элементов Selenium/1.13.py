# Откройте сайт при помощи selenium;
# Решите уравнение на странице;
# Найдите и выберите в  выпадающем списке элемент с числом, 
# которое у вас получилось после решения уравнения;
# Нажмите на кнопку;
# Скопируйте число и вставьте в поле ответа.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


with webdriver.Chrome() as browser:
    browser.get("http://parsinger.ru/selenium/6/6.html")
    answer = ((12434107696 * 3) * 2) + 1
    browser.find_element(By.XPATH, f"//option[text()='{answer}']").click()
    browser.find_element(By.ID, "sendbutton").click()
    time.sleep(5)