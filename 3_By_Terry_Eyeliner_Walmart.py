#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 19:46:20 2022

@author: luceroizquierdomunoz
"""

# 3_By Terry Eyeliner
# Import webdriver from selenium
import time
from datetime import datetime
from selenium import webdriver

currenttime = str(datetime.now())
# The path your driver is located
e_path = r"/Users/luceroizquierdomunoz/Downloads/geckodriver"
browser = webdriver.Firefox(executable_path=e_path)

browser.get('https://www.walmart.com/ip/Ligne-Blackstar-Intense-Liquid-Eyeliner-1-So-Black-by-By-Terry-for-Women-0-02-oz-Eyeliner/146437371')

time.sleep(3)
price = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/section/main/div/div[2]/div/div[1]/div/div/div[1]/div/div/div[2]/div/div/div[1]/span[1]/span[2]')

print("(",currenttime[0:19],")")
print(price.text)