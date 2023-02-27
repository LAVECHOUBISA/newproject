import pytest
from selenium import webdriver
from Logdetails import Loginpage

class Test_1():
    base_url="https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    userid="admin@yourstore.com"
    pass