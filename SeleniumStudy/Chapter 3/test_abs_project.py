import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"
link2 = 'http://suninjuly.github.io/registration2.html'

class TestAbs(unittest.TestCase):
    def test_seleniun_1(self):
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input3.send_keys("test@gmail.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be absolute value of a number")

    def test_seleniun_2(self):
        browser = webdriver.Chrome()
        browser.get(link2)
        input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input3.send_keys("test@gmail.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "Should be absolute value of a number")







if __name__ == "__main__":
    unittest.main()