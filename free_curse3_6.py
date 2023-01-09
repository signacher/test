import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('links', ["236895", "236896","236897", "236898", "236899", "236903","236904", "236905"])
def test_guest_should_see_login_link(browser, links):
    browser.implicitly_wait(12)
    link = f"https://stepik.org/lesson/{links}/step/1"
    browser.get(link)
    button_login = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="ember33"]')))
    button_login.click()
    field_mail = browser.find_element(By.XPATH, "//input[@name='login']")
    field_mail.send_keys("stalkersignacher@gmail.com")
    field_password = browser.find_element(By.XPATH, "//input[@name='password']")
    field_password.send_keys("зфыыыцщкв")
    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    time.sleep(6)
    WebDriverWait(browser, 12).until(EC.element_to_be_clickable((By.XPATH, '//textarea[@placeholder="Напишите ваш ответ здесь..."]')))
    text_area = browser.find_element(By.XPATH, '//textarea[@placeholder="Напишите ваш ответ здесь..."]')
    text_area.clear()
    text_area.send_keys(str(math.log(int(time.time()))))
    send_button = browser.find_element(By.XPATH, '//button[@class="submit-submission"]')
    send_button.click()
    time.sleep(5)
    WebDriverWait(browser, 12).until(EC.visibility_of_element_located((By.XPATH, "//p[@class='smart-hints__hint']")))
    message = browser.find_element(By.XPATH, "//p[@class='smart-hints__hint']")
    print(message.text)
    if __name__ == "__main__":
        unittest.main()
