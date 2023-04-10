from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.select import Select


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element(By.ID, 'num1')
    b = browser.find_element(By.ID, 'num2')

    select = Select(browser.find_element(By.ID, 'dropdown'))
    print(a.text, b.text)
    select.select_by_value(str(int(a.text) + int(b.text)))

    btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    btn.submit()

finally:
    time.sleep(10)
    browser.quit()
