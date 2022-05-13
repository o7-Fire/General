from selenium import webdriver
import time
import random
import string

emailprefix = "planecrazyarchive.tk"

def randomchar(length):
	return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
	
def createaccount(emailname, password):
	driver = webdriver.Chrome()
	action = webdriver.ActionChains(driver)
	driver.get("https://github.com/signup?user_email=" + emailname + "%40" + emailprefix + "&source=form-home-signup")
	time.sleep(13)
	emailbutton = driver.find_element_by_xpath('//*[@id="email-container"]/div[2]/button')
	action.move_to_element(emailbutton)
	emailbutton.click()
	time.sleep(2)
	
	passwordinput = driver.find_element_by_xpath('//*[@id="password"]')
	action.move_to_element(passwordinput)
	passwordinput.send_keys(password)
	time.sleep(2)
	passwordbutton = driver.find_element_by_xpath('//*[@id="password-container"]/div[2]/button')
	action.move_to_element(passwordbutton)
	passwordbutton.click()
	
	time.sleep(2)
	
	nameinput = driver.find_element_by_xpath('//*[@id="login"]')
	action.move_to_element(nameinput)
	nameinput.send_keys(emailname)
	time.sleep(2)
	namebutton = driver.find_element_by_xpath('//*[@id="username-container"]/div[2]/button')
	action.move_to_element(namebutton)
	namebutton.click()
	
	time.sleep(2)
	
	receiveemailinput = driver.find_element_by_xpath('//*[@id="opt_in"]')
	action.move_to_element(receiveemailinput)
	receiveemailinput.send_keys("n")
	time.sleep(2)
	receiveemailbutton = driver.find_element_by_xpath('//*[@id="opt-in-container"]/div[2]/button')
	action.move_to_element(receiveemailinput)
	receiveemailbutton.click()
	print(emailname + "@" + emailprefix + ":" + password)
	time.sleep(1000000)
	

print("created accounts:")
createaccount("Nexity" + randomchar(10), randomchar(20))
