import time
from math import sin, log

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
    return log(abs(12 * sin(x)))


with webdriver.Chrome() as browser:
    browser.get(link)
    button1 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button1.click()
    time.sleep(5)
    confirm = browser.switch_to.alert
    confirm.accept()
    x = int(browser.find_element(By.ID, 'input_value').text)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(calc(x))
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(10)
