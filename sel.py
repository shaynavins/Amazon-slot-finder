import time
from selenium.common.exceptions import NoSuchElementException
from twilio.rest import Client
from selenium import webdriver
from configparser import ConfigParser
import os
from configparser import ConfigParser

config = ConfigParser()
file = os.path.join(os.path.dirname(__file__), "config.ini")

config.read(file)
# This is your account number and your auth token. You can find this on your dashboard of your twilio site.
account_sid = "_________"
auth_token = '_________'

client = Client(account_sid, auth_token)

numKV = config['DATABASE']
twilionumber = numKV['twilionum']
mynumber = numKV['mynumber']
ext = 'whatsapp:'

find = config['DATABASE']
path = find['path']
print(path)
driver = webdriver.Chrome(path)

print(driver.command_executor._url)
driver.get(
    "https://www.amazon.com/gp/yourstore/home?ie=UTF8&action=sign-out&path=%2Fgp%2Fyourstore%2Fhome&ref_=nav_youraccount_signout&signIn=1&useRedirectOnSuccess=1&")

time.sleep(30)


cart = driver.find_elements_by_xpath("//*[@id='nav-cart']")[0]
cart.click()

checkout = driver.find_element_by_class_name("a-button-inner")
checkout.click()

alright = driver.find_element_by_xpath('//*[@id="a-autoid-0"]')

# if alright.is_displayed():
# alright = driver.find_element_by_class_name("a-button-inner")
# else:
# alright = driver.find_element_by_class_name("a-button")

alright.click()

not_available = driver.find_element_by_class_name("ufss-date-select-toggle-text-availability")

while True:
    try:
        driver.find_elements_by_xpath("//*[@id='shipoption-select']/div/div/div/div/div[1]/div[4]/div[1]/h3")[0]

        client.messages.create(from_=ext + twilionumber,
                               body="Hurry up to see Amazon!!!",
                               to=ext + mynumber)
    except NoSuchElementException:
        print("hello")
        time.sleep(4)
        driver.refresh()
