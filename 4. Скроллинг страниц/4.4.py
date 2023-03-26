# Прокрутка страницы - способ 4 scroll_by_amount()

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_2/')
    div = browser.find_element(By.CLASS_NAME, 'scroll_div_example')
    while True:
        ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()