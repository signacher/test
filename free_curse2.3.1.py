import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome(executable_path='C:\\Users\\Signacher\\PycharmProjects\\test\\chromedriver.exe')
driver.get("http://suninjuly.github.io/alert_accept.html")
driver.maximize_window()
button = driver.find_element(By.XPATH, "//button[@type='submit']")
button.click()
confirm = driver.switch_to.alert
confirm.accept()
x_element = driver.find_element(By.ID, "input_value")
x = int(x_element.text)
y = calc(x)
input_field = driver.find_element(By.ID, "answer")
input_field.send_keys(y)
button_sub = driver.find_element(By.XPATH, '//button[@type="submit"]')
button_sub.click()
time.sleep(6)