from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome(executable_path='C:\\Users\\Signacher\\PycharmProjects\\test\\chromedriver.exe')
driver.get('http://suninjuly.github.io/get_attribute.html')
driver.maximize_window()

x_element = driver.find_element(By.XPATH, "//img[@id='treasure']")
x = x_element.get_attribute('valuex')
y = calc(x)
print(y)
'''input x'''
field_input = driver.find_element(By.XPATH, "//input[@id='answer']")
field_input.send_keys(y)
box = driver.find_element(By.XPATH, '//input[@id="robotCheckbox"]')
box.click()

rule_box = driver.find_element(By.XPATH, '//input[@id="robotsRule"]')
rule_box.click()

button_box = driver.find_element(By.XPATH, '//button[@class="btn btn-default"]')
button_box.click()