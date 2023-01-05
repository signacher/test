import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:\\Users\\Signacher\\PycharmProjects\\test\\chromedriver.exe')

driver.get("http://suninjuly.github.io/explicit_wait2.html")
driver.maximize_window()
button = driver.find_element(By.ID, "book")
WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.XPATH, '//h5[@id="price"]'), "$100"))
button.click()
x_element = driver.find_element(By.ID, "input_value")
driver.execute_script("return arguments[0].scrollIntoView(true);", x_element)
x = int(x_element.text)
y = calc(x)
input_field = driver.find_element(By.ID, "answer")
input_field.send_keys(y)
button_submit = driver.find_element(By.ID, "solve")
button_submit.click()
time.sleep(6)