import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/get_attribute.html'


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = x_element.get_attribute("valuex")
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(calc(x))
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()
    time.sleep(10)