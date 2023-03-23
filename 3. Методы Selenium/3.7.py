# Откройте сайт с помощью Selenium;
# На сайте есть 50 кнопок, которые визуально перекрыты блоками;
# После нажатия на кнопку в id="result" появляется уникальное для каждой кнопки число;
# Цель: написать скрипт который нажимает поочерёдно все кнопки и собирает уникальные числа;
# Все полученные числа суммировать, и вставить результат в поле для ответа.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.maximize_window()
    browser.get("https://parsinger.ru/scroll/4/index.html")
    
    for i in range(2, 5):
        browser.execute_script(f"""
        var l = document.getElementsByClassName("block{i}")[0];
        l.parentNode.removeChild(l);""")
        time.sleep(1)
    
    buttons = browser.find_elements(By.XPATH, "//button[@class='btn']")
    sum_of_values = 0
    for button in buttons:
        button.click()
        sum_of_values += int(browser.find_element(By.ID, "result").text)

    print(sum_of_values)
    time.sleep(3)