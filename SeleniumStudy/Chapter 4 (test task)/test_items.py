import time

from selenium.webdriver.common.by import By

def adding_to_cart(browser):
    basket_link = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    adding_to_cart(browser)

