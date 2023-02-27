import string
import time
from random import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import random

import xutility
from selenium import webdriver
import unittest
import HtmlTestRunner
import pytest



driver=webdriver.Chrome("E:\\chromedriver.exe")
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin")
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//input[@id='Email']").clear()
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("admin@yourstore.com")
driver.find_element(By.XPATH, "//input[@id='Password']").clear()
driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("admin")
driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
driver.find_element(By.XPATH,"//a[@href='#']//p[contains(text(),'Customers')]").click()
driver.find_element(By.XPATH,"//a[@href='/Admin/Customer/List']").click()

def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars)for x in range(size))


driver.find_element(By.XPATH,"//a[normalize-space()='Add new']").click()
email=random_generator() + "@gmail.com"
a=driver.find_element(By.ID,"Email")
a.send_keys(email)
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("123")
driver.find_element(By.ID,"FirstName").send_keys("lave")
driver.find_element(By.ID,"LastName").send_keys("choubisa")
driver.find_element(By.ID,"Gender_Male").click()
#Date
#driver.find_element(By.XPATH,"//span[@aria-label='select']").click()
#next_btn=driver.find_element(By.XPATH,"//a[@aria-label='Next']")
#year_month=driver.find_element(By.XPATH,"//a[@aria-live='assertive']")
#while year_month.text != "January 2023":
   # next_btn.click()
    #time.sleep(2)
#date=driver.find_element(By.XPATH,"//*[@id='140a0f17-dc41-4ab3-9e9b-8e24907de09c_cell_selected']/a")
#date.click()

driver.find_element(By.XPATH,"//input[@id='Company']").send_keys("Thotnr consulting")
driver.find_element(By.XPATH,"//input[@id='IsTaxExempt']").click()
hobby=driver.find_elements(By.XPATH,"//input[@type='checkbox']")#multiple checkboxes
for h in hobby:
    h.click()
driver.find_element(By.ID,"customer_attribute_5_4").click()
Dropdown=Select(driver.find_element(By.XPATH,"//select[@id='VendorId']"))
Dropdown.select_by_visible_text("Vendor 1")
driver.find_element(By.XPATH,"//input[@id='Active']").click()
driver.find_element(By.XPATH,"//textarea[@id='AdminComment']").send_keys("Employee is added")
driver.find_element(By.XPATH,"//button[@name='save']").click()
mesg=driver.find_element(By.TAG_NAME,"Body").text
if "The new customer has been added successfully" in mesg:
    assert True==True
    driver.save_screenshot("C:\\Users\\Systems\\PycharmProjects\\Assigmentnocommerce\\screenshot"+"add customer successfull.png")
    print("Test is passed")
else:
    assert False==False
    driver.save_screenshot("C:\\Users\\Systems\\PycharmProjects\\Assigmentnocommerce\\screenshot" + "add customer successfull.png")
    print("Test is failed")






