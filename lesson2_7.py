import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    btn.submit()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, 'input_value').text

    browser.find_element(By.ID, 'answer').send_keys(calc(x))

    btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

    btn.submit()

    print(browser.switch_to.alert.text)

finally:
    time.sleep(5)
    browser.quit()
