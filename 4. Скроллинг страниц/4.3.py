# Прокрутка содержимого страницы - способ 3 ActionChains()

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    target = browser.find_element(By.ID, 'like')
    actions = ActionChains(browser).move_to_element(target).click().perform()