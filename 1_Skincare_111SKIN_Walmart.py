#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 19:23:05 2022

@author: luceroizquierdomunoz
"""

# Product: 1_Skincare 111SKIN
# Company: WALMART
# Import webdriver from selenium
import time
from datetime import datetime
from selenium import webdriver

currenttime = str(datetime.now())

# The path your driver is located
e_path = r"/Users/luceroizquierdomunoz/Downloads/geckodriver"
browser = webdriver.Firefox(executable_path=e_path)

browser.get('https://www.walmart.com/ip/111Skin-Rose-Gold-Brightening-Facial-Treatment-Mask-5-Masks/779592090')

time.sleep(3)
price = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/section/main/div/div[2]/div/div[1]/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/span/span[2]')
print("(",currenttime[0:19],")")
print(price.text)
8