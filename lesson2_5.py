import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, 'firstname').send_keys('Me')
    browser.find_element(By.NAME, 'lastname').send_keys('Me')
    browser.find_element(By.NAME, 'email').send_keys('me@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
    file = os.path.join(current_dir, 'f.txt')

    browser.find_element(By.ID, 'file').send_keys(file)

    btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    btn.submit()

    # time.sleep(2)

    # browser.switch_to.alert.accept()

finally:
    time.sleep(5)
    browser.quit()
