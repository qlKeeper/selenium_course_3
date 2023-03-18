from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get("http://parsinger.ru/selenium/1/1.html")
    time.sleep(1)
    forms = browser.find_elements(By.CLASS_NAME, "form")
    for form in forms:
        form.send_keys("Test")
        time.sleep(0.5)
    browser.find_element(By.ID, "btn").click()
    time.sleep(4)