import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    input1 = int(browser.find_element(By.ID, 'num1').text)
    input1 += int(browser.find_element(By.ID, 'num2').text)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(input1))
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()
    time.sleep(10)