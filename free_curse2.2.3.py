from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
driver = webdriver.Chrome(executable_path='C:\\Users\\Signacher\\PycharmProjects\\test\\chromedriver.exe')
driver.get('http://suninjuly.github.io/file_input.html')
driver.maximize_window()

field_input_first = driver.find_element(By.XPATH, "//input[@name='firstname']")
field_input_first.send_keys("Alex")
field_input_second = driver.find_element(By.XPATH, "//input[@name='lastname']")
field_input_second.send_keys("Telnov")
field_input_mail = driver.find_element(By.XPATH, "//input[@name='email']")
field_input_mail.send_keys("Telnov@mail.ru")
current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir)
file_path = os.path.join(current_dir, 'file.txt')
print(file_path)
element = driver.find_element(By.XPATH, "//input[@type='file']")
element.send_keys(file_path)
button_box = driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
button_box.click()
time.sleep(5)