from selenium import webdriver
from time import sleep 
import time 
from Credentials import username,password

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#opens the main website of teams 


driver.get('https://www.microsoft.com/en-in/microsoft-365/microsoft-teams/group-chat-software')
time.sleep(7)
#waits for 7 seconds to avoid suspicion


driver.find_element_by_xpath('//a[@class="c-button f-secondary ow-slide-in ow-slide-in-2 xs-ow-mr-0 ow-mt-10 ow-txt-trans-upper ow-bvr-signin"]').click()
#finds the login icon


driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
#switches to the other tab in order to login and first sees the username login


driver.switch_to_active_element().send_keys(username)
time.sleep(2)
driver.find_element_by_xpath('//input[@class="button ext-button primary ext-primary"]').click()
print('Username Entered...')
time.sleep(5)
#logs in the username and prints it in order to show that I have done it and waits for 5


driver.switch_to_active_element().send_keys(password)
time.sleep(2)
driver.find_element_by_xpath('//input[@id="idSIButton9"]').click()
print('Password Entered...')
time.sleep(6)
#does the same thing to enter the password and the username and then clicks the login icon 


time.sleep(4)
driver.find_element_by_xpath('//input[@class="button ext-button primary ext-primary"]').click()
#yes button always remember


print('Yes Button Has Been Clicked...')
time.sleep(10)
#yes remember me everytime I login 


driver.find_element_by_xpath('/html/body/promote-desktop/div/div/div/div[1]/div[2]/div/a').click()
time.sleep(10)
print('Using Web App')
#displays that Iam using teams