import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/selects1.html')
number_1 = browser.find_element(By.XPATH, '//span[@id="num1"]')
num1 = int(number_1.text)
number_2 = browser.find_element(By.XPATH, '//span[@id="num2"]')
num2 = int(number_2.text)
summa = str(num1 + num2)
print(summa)
select = Select(browser.find_element(By.XPATH, '//select[@class="custom-select"]'))
select.select_by_visible_text(summa)
browser.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(10)