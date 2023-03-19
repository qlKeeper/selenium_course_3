# Открываем сайт с помощью selenium;
# Получаем значения всех элементов выпадающего списка;
# Суммируем(плюсуем) все значения;
# Вставляем получившийся результат в поле на сайте;
# Нажимаем кнопку и копируем длинное число;
# Вставляем конечный результат в поле ответа.


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/7/7.html")
    values = browser.find_elements(By.TAG_NAME, "option")
    sum_of_values = 0
    for value in values:
        sum_of_values += int(value.text)
    time.sleep(0.5)
    browser.find_element(By.ID, "input_result").send_keys(sum_of_values)
    time.sleep(0.5)
    browser.find_element(By.ID, "sendbutton").click()
    time.sleep(5)