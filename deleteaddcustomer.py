from random import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import random

import xutility
from selenium import webdriver
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
driver.find_element(By.XPATH,"//body[1]/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[6]/td[7]/a[1]").click()
driver.save_screenshot("C:\\Users\\Systems\\PycharmProjects\\Assigmentnocommerce\\screenshot"+"Delete candidate name.png")
driver.find_element(By.XPATH,"//span[@id='customer-delete']").click()