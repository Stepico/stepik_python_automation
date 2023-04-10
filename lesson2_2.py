from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    calc_answer = browser.find_element(By.ID, 'answer')
    calc_answer.send_keys(y)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()

    btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    btn.submit()

finally:
    time.sleep(10)
    browser.quit()
