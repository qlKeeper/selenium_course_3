# Откройте сайт;
# Извлеките данные из каждого  второго тега <p>;
# Сложите все значения, их всего 100 шт;
# Напишите получившийся результат в поле ответа.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://parsinger.ru/selenium/3/3.html")
    numbers = browser.find_elements(By.XPATH, "//p[2]")
    sum_of_numbers = 0
    for number in numbers:
        sum_of_numbers += int(number.text)
finally:
    print(sum_of_numbers)
    browser.quit()