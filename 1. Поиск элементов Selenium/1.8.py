# Откройте сайт;
# Извлеките данные из каждого тега <p>;
# Сложите все значения, их всего 300 шт;
# Напишите получившийся результат в поле ниже.


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get("http://parsinger.ru/selenium/3/3.html")
    values = browser.find_elements(By.TAG_NAME, 'p')
    sum_of_values = 0
    for value in values:
        sum_of_values += int(value.text)
    print(sum_of_values)