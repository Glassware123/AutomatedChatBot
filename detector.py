# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
import logging
from selenium.common.exceptions import NoSuchElementException

def check_exists_by_xpath():
    try:
        web.find_elements_by_xpath('//span[contains(@class,"chat-subtitle-text")]')
    except NoSuchElementException:
        return False
    return True

def addLog():
    logging.basicConfig(filename='lastseen.log',level=logging.INFO)
    logging.info("BenSirket:" + datetime.strftime(now, "%c")+"\n" )
    print "log"

def checkStatusBar():
    elem1 = web.find_element_by_xpath('//span[contains(@class,"emojitext O90ur")]')
    return elem1

web = webdriver.Firefox()
web.get('http://web.whatsapp.com')
time.sleep(10)

elem = web.find_element_by_xpath('//span[contains(text(),"BenSirket")]')
elem.click()
while True:
    time.sleep(10)
    print check_exists_by_xpath()
    if(check_exists_by_xpath()):
        try:
            elem1 = checkStatusBar()
            now = datetime.now()
            print elem1
            addLog()
        except:
            time.sleep(10)

