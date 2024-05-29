# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from skpy import Skype, SkypeChats
import unittest, time, re
import pyautogui
import datetime
##import ConfigParser
import configparser




options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
driver = webdriver.Chrome(r"C:\Users\amit\Desktop\programe\chromedriver.exe",chrome_options=options)
driver.implicitly_wait(30)
base_url = "https://www.google.com/"

driver.maximize_window()


count =5

phone_list=['0965396701','0958781005']
phone=phone_list[0]

account=['m30','g416','m15','G530']
account_1=account[0]



def login(account_1):
    if account_1 == 'm30':
        driver.get("http://192.168.125.1/info/Login.html?")
        driver.find_element_by_name("admin_Password").send_keys("Admin1234567")

    elif account_1 =='g416':
        driver.get("http://192.168.0.1/info/Login.html?")
        driver.find_element_by_name("admin_Password").send_keys("Admin1234567")
    elif account_1 =='m15':
        driver.get("http://192.168.0.1/info/Login.html?")
        driver.find_element_by_name("admin_Password").send_keys("admin123")
    elif account_1 =='G530':
        driver.get("http://192.168.125.1/info/Login.html?")
        driver.find_element_by_name("admin_Password").send_keys("Admin1234567")
    driver.find_element_by_id("logIn_btn").click()
    time.sleep(2)







driver.get("http://192.168.125.1/Cellular_Sms.html")

def message(count,phone):

    for i in range (0,message):
        driver.find_element_by_id("createButton").click()
        driver.find_element_by_name("PhoneNumber").send_keys(phone)
        driver.find_element_by_name("MessageText").send_keys(i)
        driver.find_element_by_id("save_buttonFocus").click()
        time.sleep(10)
        driver.find_element_by_id("popalert_ok").click()
        time.sleep(2)







message(count,phone)
login(account_1)











'''
for i in range(1,441):
#for i in range(1,10):
    i=str(i)

    path="//*[@id='SearchTimeZoneWrap']//li["+i+"]/a"
    txt= driver.find_element_by_xpath(path).text
    print(txt)


txt= driver.find_element_by_xpath("//*[@id='SearchTimeZoneWrap']//li["+i+"]/a").text
print(txt)
'''





