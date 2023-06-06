import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


link = "http://suninjuly.github.io/file_input.html"

def file():
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    return file_path

def filling_out_the_form(class_instance_webdriver):
    input1 = browser.find_element(By.XPATH, "//input[@placeholder='Enter first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//input[@placeholder='Enter last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//input[@placeholder='Enter email']")
    input3.send_keys("test@gmail.com")
    input4 = browser.find_element(By.CSS_SELECTOR, "#file")
    input4.send_keys(file())
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

with webdriver.Chrome() as browser:

    browser.get(link)
    filling_out_the_form(browser)
    time.sleep(20)

