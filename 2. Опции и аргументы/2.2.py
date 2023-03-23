# Запуск браузера в скрытом режиме

from selenium import webdriver
from selenium.webdriver.common.by import By

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless')

with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)
    a = browser.find_element(By.TAG_NAME, 'a')
    print(a.get_attribute('href'))


'''Преимущества запуска браузера в фоновом режиме.

Отсутствует отрисовка содержимого, тем самым потребует меньше ресурсов.
Работает быстрее, т.к. потребляет меньше потому что ему ничего не нужно обрисовывать.
Не занимает место на экране, и не мешает вашей работе во время выполнения скрипта.
Использование --headless может значительно ускорить работу парсера, 
на относительно слабых машинах.'''