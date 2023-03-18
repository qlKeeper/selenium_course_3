# Откройте сайт;
# Установите все чек боксы в положение checked при помощи selenium и метода click();
# Когда все чек боксы станут активны, нажмите на кнопку;
# Скопируйте число которое появится на странице;
# Результат появится в <p id="result">Result</p>;
# Вставьте число в поле для ответа.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    browser = webdriver.Chrome()
    browser.get("https://parsinger.ru/selenium/4/4.html")
    check_boxes = browser.find_elements(By.CSS_SELECTOR, "[type='checkbox']")
    time.sleep(1)
    for check_box in check_boxes:
        check_box.click()
    browser.find_element(By.CSS_SELECTOR, "[value='Отправить']").click()

finally:
    time.sleep(4)
    browser.quit()