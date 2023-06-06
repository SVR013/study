import time
import time
from math import sin, log
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
    return log(abs(12 * sin(x)))


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = browser.find_element(By.ID, 'book')
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button.click()
    x = int(browser.find_element(By.ID, 'input_value').text)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(calc(x))
    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()
    time.sleep(10)