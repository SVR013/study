import pytest
from selenium.webdriver.common.by import By
import time
from config import PASSWORD, LOGIN
import math

list_number = ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905']
@pytest.mark.parametrize('numbers', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, numbers):
    browser.implicitly_wait(5)
    print(numbers)
    link = f"https://stepik.org/lesson/{numbers}/step/1"
    browser.get(link)
    button = browser.find_element(By.ID, "ember33")
    button.click()
    input1 = browser.find_element(By.ID, 'id_login_email')
    input1.send_keys(LOGIN)
    input2 = browser.find_element(By.ID, 'id_login_password')
    input2.send_keys(PASSWORD)
    button_login = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader")
    button_login.click()
    time.sleep(5)
    textarea = browser.find_element(By.XPATH, "//textarea[@placeholder='Напишите ваш ответ здесь...']")
    textarea.send_keys(str(math.log(int(time.time()))))
    button_task = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
    button_task.click()
    correct = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint')
    assert correct.text == 'Correct!', f'{correct.text}'