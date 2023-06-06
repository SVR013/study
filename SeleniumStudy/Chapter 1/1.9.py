import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

letters = string.ascii_lowercase

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        random_word = ''.join(random.choice(letters) for _ in range(8))
        element.send_keys(random_word)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()