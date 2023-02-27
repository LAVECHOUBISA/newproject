from selenium.webdriver.common.by import By

import xutility
from selenium import webdriver
import unittest
import HtmlTestRunner
import pytest

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
       cls.driver=webdriver.Chrome("E:\\chromedriver.exe")
       cls.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin")
    def test_login(self):
           self.file="C:\\Users\\Systems\\Desktop\\admin no commerce.xlsx"
           self.rows=xutility.getrowcount(self.file,"Sheet1")
           for r in range(2,self.rows+1):
              username=xutility.readrow(self.file,"Sheet1",r,1)
              password=xutility.readrow(self.file,"Sheet1",r,2)
              self.driver.find_element(By.XPATH, "//input[@id='Email']").clear()
              self. driver.find_element(By.XPATH,"//input[@id='Email']").send_keys(username)
              self. driver.find_element(By.XPATH, "//input[@id='Password']").clear()
              self.driver.find_element(By.XPATH, "//input[@id='Password']").send_keys(password)
              self. driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
              self.assertTrue( "Dashboard / nopCommerce administration"==self.driver.title)
              xutility.writecolumn(self.file,"Sheet1",r,3,"Pass")
              self.driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()


    def test_login1(self):
           self.file="C:\\Users\\Systems\\Desktop\\admin no commerce.xlsx"
           self.rows=xutility.getrowcount(self.file,"Sheet1")
           for r in range(3,self.rows+1):
              username=xutility.readrow(self.file,"Sheet1",r,1)
              password=xutility.readrow(self.file,"Sheet1",r,2)
              self.driver.find_element(By.XPATH, "//input[@id='Email']").clear()
              self. driver.find_element(By.XPATH,"//input[@id='Email']").send_keys(username)
              self. driver.find_element(By.XPATH, "//input[@id='Password']").clear()
              self.driver.find_element(By.XPATH, "//input[@id='Password']").send_keys(password)
              self. driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
              self.assertEqual("Dashbo / nopCommerce administration", self.driver.title,"message is invalid")
              xutility.writecolumn(self.file,"Sheet1",r,3,"Fail")

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\Systems\\PycharmProjects\\Assigmentnocommerce\\Reports\\Html report"))