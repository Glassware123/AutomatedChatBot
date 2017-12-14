from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




web = webdriver.Firefox()
web.get('http://web.whatsapp.com')
time.sleep(5)

try:
    elem = web.find_element_by_xpath('//span[contains(text(),"XYZ")]')
    elem.click()
    elem1 = web.find_elements_by_xpath('//div[contains(@class,"input")]')
    textarea=elem1[0]
    while True:
        textarea.send_keys("18 eyl pzt")
        textarea.send_keys(Keys.ENTER);
        time.sleep(1)
except:
    web.close()
