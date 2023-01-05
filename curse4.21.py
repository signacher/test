from selenium import webdriver
import time
import datetime

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\Signacher\\PycharmProjects\\test\\chromedriver.exe')
driver.get('https://demoqa.com/date-picker')
driver.maximize_window()

new_data = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
'''Clear field'''
new_data.send_keys(Keys.BACKSPACE*10)
time.sleep(3)
'''now data + 10 days'''
future_date = datetime.datetime.today() + datetime.timedelta(days=10)
print(future_date)
future_date = future_date.strftime('%d/%m/%y')
print(future_date)
'''input future date'''
new_data.send_keys(future_date)
new_data.send_keys(Keys.ENTER)
time.sleep(5)
driver.close()