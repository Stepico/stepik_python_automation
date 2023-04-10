import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price_tag = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    btn = browser.find_element(By.ID, 'book')
    btn.click()

    x = browser.find_element(By.ID, 'input_value').text

    browser.find_element(By.ID, 'answer').send_keys(calc(x))

    solve_btn = browser.find_element(By.ID, 'solve')

    solve_btn.click()

    print(browser.switch_to.alert.text)

finally:
    time.sleep(5)
    browser.quit()
