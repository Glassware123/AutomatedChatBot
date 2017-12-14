# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
from selenium.common.exceptions import NoSuchElementException

global elem1

def check_exists_by_xpath():
    try:
        web.find_elements_by_xpath('//span[contains(@class,"chat-subtitle-text")]')
    except NoSuchElementException:
        return False
    return True


web = webdriver.Firefox()
web.get('http://web.whatsapp.com')
time.sleep(10)

try:
    elem = web.find_element_by_xpath('//span[contains(text(),"XYZ")]')
    elem.click()
    while True:
        time.sleep(10)
        print check_exists_by_xpath()
        if(check_exists_by_xpath()):
            elem1 = web.find_elements_by_xpath('//span[contains(@class,"chat-subtitle-text")]')
            now = datetime.now()
            print elem1
            print elem1[0].text == "çevrimiçi"
            if (elem1[0].text.decode("utf-8") == "çevrimiçi"):
                print "log"
                txt = open("log.txt", "a")
                txt.write("XYZ" + datetime.strftime(now,"%c"))

except Exception as e:
    print e.message
