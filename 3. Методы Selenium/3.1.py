# Cookies на практике
# Метод .get_cookies() который получает список всех cookie на странице. 

from pprint import pprint
from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://ya.ru/')
    cookies = webdriver.get_cookies()
    for cookie in cookies:
        pprint(cookie['name'])