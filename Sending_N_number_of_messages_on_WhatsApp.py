'''
This script sends N(the value of N can be chosen by the user) number of messages to any contact or group on WhatsApp.
Requirements -
1. Python 3
  You can download Python 3 from : https://www.python.org/downloads
2. Selenium webdriver
  Here is a guide on how you can do this : http://seleniummaster.com/sitecontent/index.php/selenium-web-driver-menu/selenium-test-automation-with-python-menu/186-how-to-install-selenium-python-webdriver 
3. Chrome Driver(optional)
  Here is a guide on how you can do this : https://sites.google.com/a/chromium.org/chromedriver/getting-started 
'''
from selenium import webdriver # you need to have selenium webdriver module installed.
Browser = webdriver.Chrome() # you will need Chrome Driver for it. If you do not have Chrome Driver then you can replace Chrome by Firefox
Browser.get('http://web.whatsapp.com') # wait while your selected browser is launched and the QR code is loaded.
input("Scan the QR code. Enter something when done: ") # scan the QR code from your mobile and when done enter any key
name = Browser.find_element_by_xpath('//span[contains(text(),"Name Of Group Or Friend")]') # write the contact name or group name in quotes.
name.click()
box = Browser.find_elements_by_class_name('input')
N = int(input("Enter the number of times the message should be sent: ")) # enter the number of times you want the message to be sent. 
for i in range(N):
  box[1].send_keys('Here goes your message') # type your message in the quotes.
  Browser.find_element_by_class_name('send-container').click()
