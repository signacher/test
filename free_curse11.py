# -*- coding: utf8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = " http://suninjuly.github.io/registration1.html"
    first_name = 'alex'
    last_name = 'ivanov'
    email = 'skdhlef@corfho.ru'
    browser = webdriver.Chrome()
    browser.get(link)


#     # Ваш код, который заполняет обязательные поля
    input_1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    input_1.send_keys(first_name)
    input_2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    input_2.send_keys(last_name)
    input_3 = browser.find_element(By.XPATH,"//input[@placeholder='Input your email']")
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
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
#
finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
#     # закрываем браузер после всех манипуляций
    browser.quit()