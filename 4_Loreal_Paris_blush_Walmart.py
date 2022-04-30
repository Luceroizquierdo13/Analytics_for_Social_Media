#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 19:51:42 2022

@author: luceroizquierdomunoz
"""

# 4_Loreal Paris blush
# Import webdriver from selenium
import time
from datetime import datetime
from selenium import webdriver

currenttime = str(datetime.now())
# The path your driver is located
e_path = r"/Users/luceroizquierdomunoz/Downloads/geckodriver"
browser = webdriver.Firefox(executable_path=e_path)

browser.get('https://www.cvs.com/shop/l-oreal-paris-true-match-super-blendable-blush-prodid-1016136?skuid=320706&cgaa=QWxsb3dHb29nbGVUb0FjY2Vzc0NWU1BhZ2Vz')

time.sleep(3)
price = browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/main/div[2]/div/div[3]/div[2]/div[3]/div[1]/section/div/div/section/div/div[2]/div')

print("(",currenttime[0:19],")")
print(price.text)