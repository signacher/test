from selenium import webdriver
import time
from selenium.webdriver.common.by import By
login = 'at@pryaniky.ru'
password = 'qw123456'
driver = webdriver.Chrome(executable_path='C:\\Users\\Signacher\\PycharmProjects\\test\\chromedriver.exe')
driver.get ('https://ideasperi.app.pryaniky.com/')
driver.maximize_window()
user_name = driver.find_element(By.XPATH, "//*[@id='LOGINUSERNAME']")
user_name.send_keys(login)
password_name = driver.find_element(By.XPATH, '//*[@id="LOGINPASSWORD"]')
password_name.send_keys(password)
login_button = driver.find_element(By.XPATH, '//*[@id="LOGINENTERBUTTON"]')
login_button.click()
time.sleep(15)
driver.close()

