import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = " http://suninjuly.github.io/registration1.html"
        first_name = 'alex'
        last_name = 'ivanov'
        email = 'skdhlef@corfho.ru'
        browser = webdriver.Chrome()
        browser.get(link)
        input_1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        input_1.send_keys(first_name)
        input_2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input_2.send_keys(last_name)
        input_3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input_3.send_keys(email)
        #     # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        #
        #     # Проверяем, что смогли зарегистрироваться
        #     # ждем загрузки страницы
        time.sleep(1)
        #
        #     # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        #     # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Ok")

    def test_abs2(self):
        link = " http://suninjuly.github.io/registration2.html"
        first_name = 'alex'
        last_name = 'ivanov'
        email = 'skdhlef@corfho.ru'
        browser = webdriver.Chrome()
        browser.get(link)
        input_1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        input_1.send_keys(first_name)
        input_2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input_2.send_keys(last_name)
        input_3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input_3.send_keys(email)
        #     # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        #
        #     # Проверяем, что смогли зарегистрироваться
        #     # ждем загрузки страницы
        time.sleep(1)
        #
        #     # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        #     # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Ok")


if __name__ == "__main__":
    unittest.main()