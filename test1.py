from selenium.webdriver.common.by import By

import xutility
from selenium import webdriver
import unittest
import HtmlTestRunner
import pytest



driver=webdriver.Chrome("E:\\chromedriver.exe")
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin")
file="C:\\Users\\Systems\\Desktop\\admin no commerce.xlsx"
rows=xutility.getrowcount(file,"Sheet1")
for r in range(2,rows+1):
    username=xutility.readrow(file,"Sheet1",r,1)
    password=xutility.readrow(file,"Sheet1",r,2)
    driver.find_element(By.XPATH, "//input[@id='Email']").clear()
    driver.find_element(By.XPATH,"//input[@id='Email']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@id='Password']").clear()
    driver.find_element(By.XPATH, "//input[@id='Password']").send_keys(password)
    driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
    if driver.title=="Dashboard / nopCommerce administration":
       driver.save_screenshot("C:\\Users\\Systems\\PycharmProjects\\Assigmentnocommerce\\screenshot"+"valid credential.png")
       print("Test is pass")
       xutility.writecolumn(file,"Sheet1",r,3,"Pass")
    else:
      print("Test is fail")
      driver.save_screenshot("C:\\Users\\Systems\\PycharmProjects\\Assigmentnocommerce\\screenshot"+"Invalid credential.png")
      xutility.writecolumn(file, "Sheet1", r, 3, "Fail")

    driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()


