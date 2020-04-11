import time
from selenium.common.exceptions import NoSuchElementException

from twilio.rest import Client
from selenium import webdriver


account_sid = 'ACa2252f332f0ca494f3f0e8ffcdaf6230'
auth_token = '9ee3aed574a9da61417254c06e5392b2'

client = Client(account_sid, auth_token)


driver = webdriver.Chrome("/Users/vinothrajasekaran/Downloads/chromedriver")

print(driver.command_executor._url)
driver.get(
    "https://www.amazon.com/gp/yourstore/home?ie=UTF8&action=sign-out&path=%2Fgp%2Fyourstore%2Fhome&ref_=nav_youraccount_signout&signIn=1&useRedirectOnSuccess=1&")

time.sleep(50)

from_whatsapp_number = 'whatsapp:+14155238886'
to_number_my = 'whatsapp:+1USNUMBER>'

cart = driver.find_element_by_id("nav-cart")
cart.click()

checkout = driver.find_element_by_class_name("a-button-inner")
checkout.click()

alright = driver.find_element_by_class_name("a-button-inner")

if alright.is_displayed():
    alright = driver.find_element_by_class_name("a-button-inner")
else:
    alright = driver.find_element_by_class_name("a-button")

alright.click()

not_available = driver.find_element_by_class_name("ufss-date-select-toggle-text-availability")

while True:
    try:
        driver.find_element_by_class_name("ufss-grid-row-title")

        client.messages.create(body="Hurry up to see Amazon!!!",
                           from_=from_whatsapp_number,
                           to=to_number_my)
    except NoSuchElementException:
        print("hello")
        time.sleep(4)
        driver.refresh()


