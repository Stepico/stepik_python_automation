import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    btn.submit()

    confirm = browser.switch_to.frame
    confirm.accept()

    x = browser.find_element(By.ID, 'input_value').text

    browser.find_element(By.ID, 'answer').send_keys(calc(x))

    wait = WebDriverWait(browser, 10)
    subm = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))

    subm.click()

    print(browser.switch_to.alert.text)

finally:
    time.sleep(5)
    browser.quit()
