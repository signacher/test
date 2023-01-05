# -*- coding: utf8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
login = 'standard_user'
password = 'secret_sauce'
driver = webdriver.Chrome(executable_path='C:\\Users\\Signacher\\PycharmProjects\\test\\chromedriver.exe')
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
'''Вводим логин'''
user_name = driver.find_element(By.XPATH, "//input[@data-test='username']")
user_name.send_keys(login)
print('Input login')
'''Вводим пароль'''
password_name = driver.find_element(By.XPATH, "//input[@data-test='password']")
password_name.send_keys(password)
print('Input password')
'''Нажимаем кнопку логин'''
login_button = driver.find_element(By.XPATH, "//input[@type='submit']")
login_button.click()
print('Click login Button')
'''проверка перехода на главную страницу'''
text_product = driver.find_element(By.XPATH, "//span[@class='title']")
value_text_product = text_product.text
value_text_product = 'PRODUCTS'
print('assert OK')
'''info product #1'''
product1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product1= product1.text
print(value_product1)
price_product1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product1 = price_product1.text
print(value_price_product1)
'''Add cart product1'''
select_product1=driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product1.click()
print('select product1')
'''info product #2'''
product2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
value_product2 = product2.text
print(value_product2)
price_product2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
value_price_product2 = price_product2.text
print(value_price_product2)
'''Add cart product2'''
select_product2=driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
select_product2.click()
print('select product 2')

cart=driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart.click()
print('enter cart')
'''Info cart product1'''
cart_product1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_cart_product1 = cart_product1.text
print(value_cart_product1)
assert value_product1 == value_cart_product1
print('Info cart product1 GOOD')
price_cart_product1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_cart_product1 = price_cart_product1.text
print(value_price_cart_product1)
assert value_price_product1 == value_price_cart_product1
print('Info cart price product1 GOOD')
'''Info cart product2'''
cart_product2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
value_cart_product2 = cart_product2.text
print(value_cart_product2)
assert value_cart_product2 == value_product2
print('Info cart product2 GOOD')
price_cart_product2 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_price_cart_product2 = price_cart_product2.text
print(value_price_cart_product2)
assert value_price_cart_product2 == value_price_product2
print('Info cart price product2 GOOD')

checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print('Click checkout')

'''Select user INFO'''
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys('Alexey')
print('Input first_name')

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys('Telnov')
print('Input last_name')

zip = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip.send_keys('111111')
print('Input zip')

continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print('Click continue_button')

'''Info finish product1'''
finish_product1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_finish_product1 = finish_product1.text
print(value_finish_product1)
assert value_product1 == value_finish_product1
print('Info finish product1 GOOD')
price_finish_product1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_finish_product1 = price_finish_product1.text
print(value_price_finish_product1)
assert value_price_product1 == value_price_finish_product1
print('Info finish price product1 GOOD')
'''Info finish product2'''
finish_product2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
value_finish_product2 = finish_product2.text
print(value_finish_product2)
assert value_finish_product2 == value_product2
print('Info finish product2 GOOD')
price_finish_product2 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_price_finish_product2 = price_finish_product2.text
print(value_price_finish_product2)
assert value_price_finish_product2 == value_price_product2
print('Info finish price product2 GOOD')

summury_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]")
value_summury_price = summury_price.text
print(value_summury_price)
item_price1 = float(value_price_product1[1:])
item_price2 = float(value_price_product2[1:])
item_price = str(item_price1 + item_price2)
item_price_total = "Item total: $" + item_price
assert value_summury_price == item_price_total
print('Total price GOOD')
time.sleep(2)
driver.close()
