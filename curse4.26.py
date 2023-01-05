# -*- coding: utf8 -*-
'''Сделал без ООП'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
login = 'standard_user'
password = 'secret_sauce'

def product_all(locator_product,locator_price,locator_addcart,locator_cartproduct,locator_cartprice,locator_finish_product,locator_finish_price):
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
    '''Click login'''
    login_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    login_button.click()
    print('Click login Button')
    '''проверка перехода на главную страницу'''
    text_product = driver.find_element(By.XPATH, "//span[@class='title']")
    value_text_product = text_product.text
    value_text_product = 'PRODUCTS'
    print('Assert OK')
    product1 = driver.find_element(By.XPATH, locator_product)
    value_product = product1.text
    print(value_product)
    price_product = driver.find_element(By.XPATH, locator_price)
    value_price_product = price_product.text
    print(value_price_product)
    '''Add cart product'''
    select_product = driver.find_element(By.XPATH,locator_addcart )
    select_product.click()
    print('Select product')
    '''Click button cart '''
    cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart.click()
    print('Enter cart')
    '''Info cart product'''
    cart_product = driver.find_element(By.XPATH, locator_cartproduct)
    value_cart_product = cart_product.text
    print(value_cart_product)
    assert value_product == value_cart_product
    print('Info cart product GOOD')
    price_cart_product = driver.find_element(By.XPATH, locator_cartprice)
    value_price_cart_product = price_cart_product.text
    print(value_price_cart_product)
    assert value_price_product == value_price_cart_product
    print('Info cart price product GOOD')

    '''Checkout'''
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
    '''Info finish product'''
    finish_product = driver.find_element(By.XPATH, locator_finish_product )
    value_finish_product = finish_product.text
    print(value_finish_product)
    assert value_product == value_finish_product
    print('Info finish product GOOD')
    price_finish_product = driver.find_element(By.XPATH, locator_finish_price)
    value_price_finish_product = price_finish_product.text
    print(value_price_finish_product)
    assert value_price_product == value_price_finish_product
    print('Info finish price product GOOD')
    '''Click finish button'''
    finich_button = driver.find_element(By.XPATH, '//button[@id="finish"]')
    finich_button.click()
    complete = driver.find_element(By.XPATH, "//span[@class='title']")
    complete_text = complete.text
    assert complete_text == 'CHECKOUT: COMPLETE!'
    print('Assert ok')
    print('Test success')

print('Приветствую тебя в нашем интернет магазине')
print('''Выбирите один из следующих товаров и укажите его номер 
1 - Sauce Labs Backpack
2 - Sauce Labs Bike Light
3 - Sauce Labs Bolt T-Shirt
4 - Sauce Labs Fleece Jacket
5 - Sauce Labs Onesie
6 - Test.allTheThings() T-Shirt (Red)''')
product_number = input()
match product_number:
    case '1':
        print('Select 1')
        locator_product = "//a[@id='item_4_title_link']"
        locator_price = "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div"
        locator_addcart = "//button[@id='add-to-cart-sauce-labs-backpack']"
        locator_cartproduct = "//a[@id='item_4_title_link']"
        locator_cartprice = "//div[@class='inventory_item_price']"
        locator_finish_product = "//a[@id='item_4_title_link']"
        locator_finish_price = "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div"
        product_all(locator_product,locator_price,locator_addcart,locator_cartproduct,locator_cartprice,locator_finish_product,locator_finish_price)
    case '2':
        print('Select 2')
        locator_product = "//a[@id='item_0_title_link']"
        locator_price = '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div'
        locator_addcart = "//button[@id='add-to-cart-sauce-labs-bike-light']"
        locator_cartproduct = "//a[@id='item_0_title_link']"
        locator_cartprice = "//div[@class='inventory_item_price']"
        locator_finish_product = "//a[@id='item_0_title_link']"
        locator_finish_price = "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div"
        product_all(locator_product,locator_price,locator_addcart,locator_cartproduct,locator_cartprice,locator_finish_product,locator_finish_price)
    case '3':
        print('Select 3')
        locator_product = "//a[@id='item_1_title_link']"
        locator_price = "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div"
        locator_addcart = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
        locator_cartproduct = "//a[@id='item_1_title_link']"
        locator_cartprice = '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div'
        locator_finish_product = "//a[@id='item_1_title_link']"
        locator_finish_price = '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div'
        product_all(locator_product,locator_price,locator_addcart,locator_cartproduct,locator_cartprice,locator_finish_product,locator_finish_price)
    case '4':
        print('Select 4')
        locator_product = "//a[@id='item_5_title_link']"
        locator_price ='//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div'
        locator_addcart = '//button[@id="add-to-cart-sauce-labs-fleece-jacket"]'
        locator_cartproduct = "//a[@id='item_5_title_link']"
        locator_cartprice = '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div'
        locator_finish_product = "//a[@id='item_5_title_link']"
        locator_finish_price = '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div'
        product_all(locator_product,locator_price,locator_addcart,locator_cartproduct,locator_cartprice,locator_finish_product,locator_finish_price)
    case '5':
        print('Select 5')
        locator_product = "//a[@id='item_2_title_link']"
        locator_price = '//*[@id="inventory_container"]/div/div[5]/div[2]/div[2]/div'
        locator_addcart = '//button[@id="add-to-cart-sauce-labs-onesie"]'
        locator_cartproduct = "//a[@id='item_2_title_link']"
        locator_cartprice = '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div'
        locator_finish_product = "//a[@id='item_2_title_link']"
        locator_finish_price = '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div'
        product_all(locator_product,locator_price,locator_addcart,locator_cartproduct,locator_cartprice,locator_finish_product,locator_finish_price)
    case '6':
        print('Select 6')
        locator_product = "//a[@id='item_3_title_link']"
        locator_price = '//*[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div'
        locator_addcart = '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]'
        locator_cartproduct = "//a[@id='item_3_title_link']"
        locator_cartprice = '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div'
        locator_finish_product = "//a[@id='item_3_title_link']"
        locator_finish_price = '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div'
        product_all(locator_product,locator_price,locator_addcart,locator_cartproduct,locator_cartprice,locator_finish_product,locator_finish_price)
    case _:
        print('Неверный номер. Попробуйте еще раз')