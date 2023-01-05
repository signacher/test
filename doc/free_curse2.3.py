import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
driver = webdriver.Chrome(executable_path='C:\\Users\\Signacher\\PycharmProjects\\test\\chromedriver.exe')
link = "https://SunInJuly.github.io/execute_script.html"
driver.get(link)
driver.maximize_window()

x_element = driver.find_element(By.ID, 'input_value')
x = int(x_element.text)
y = calc(x)

field_input = driver.find_element(By.XPATH, "//input[@id='answer']")
field_input.send_keys(y)

box = driver.find_element(By.XPATH, '//input[@id="robotCheckbox"]')
box.click()

driver.execute_script("return arguments[0].scrollIntoView(true);", box)
rule_box = driver.find_element(By.XPATH, '//input[@id="robotsRule"]')
rule_box.click()

button_box = driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
button_box.click()
time.sleep(5)
