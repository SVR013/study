import time
from math import sin, log

from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://SunInJuly.github.io/execute_script.html"


def calc(x):
    return log(abs(12 * sin(x)))


with webdriver.Chrome() as browser:

    browser.get(link)
    x = int(browser.find_element(By.ID, 'input_value').text)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(calc(x))

    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    time.sleep(20)