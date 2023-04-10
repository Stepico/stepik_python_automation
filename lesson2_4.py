from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value')
    res = calc(x.text)

    # browser.execute_script("cb = document.getElementById('input_value');cb.scrollIntoView(true)")
    browser.execute_script("window.scrollBy(0, 100);")

    browser.find_element(By.ID, 'answer').send_keys(res)

    browser.find_element(By.ID, 'robotCheckbox').click()

    browser.find_element(By.ID, 'robotsRule').click()

    btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    btn.submit()

    # time.sleep(2)

    # browser.switch_to.alert.accept()

finally:
    time.sleep(5)
    browser.quit()
