from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"

def filling_out_the_form(class_instance_webdriver):
    input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    input3.send_keys("test@gmail.com")


with webdriver.Chrome() as browser:

    browser.get(link)

    #аполняем поля
    filling_out_the_form(browser)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    time.sleep(10)
