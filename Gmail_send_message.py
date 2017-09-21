from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

capabilities = DesiredCapabilities.FIREFOX.copy()
capabilities['marionette'] = False
driver = webdriver.Firefox(capabilities=capabilities)
driver.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

emailElem = driver.find_element_by_id('identifierId').send_keys('your_login')
driver.find_element_by_id('identifierNext').click()

time.sleep(2)

password = driver.find_element_by_name('password').send_keys('your_password')
driver.find_element_by_id("passwordNext").click()

time.sleep(5)

compose = driver.find_element_by_xpath('''//div[@class='z0']//div[.='COMPOSE']''').click()

time.sleep(2)

message_to = driver.find_element_by_id(':9d').send_keys('Send to email')

time.sleep(2)

message_subject = driver.find_element_by_id(':8w').send_keys('Subject')

time.sleep(2)

message_text = driver.find_element_by_id(':9x').send_keys('Text')

# time.sleep(2)

# send_message = driver.find_element_by_id(':8m').click()
