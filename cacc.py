from selenium import webdriver
import time

emailprefix = "planecrazyarchive.tk"
def createaccount(emailname, password):
	driver = webdriver.Chrome()
	driver.get("https://github.com/signup?user_email=" + emailname + "%40" + emailprefix + "&source=form-home-signup")
	time.sleep(5)
	emailbutton = driver.find_element_by_xpath('//*[@id="email-container"]/div[2]/button')
	emailbutton.click()
	time.sleep(1)
	
	passwordinput = driver.find_element_by_xpath('//*[@id="password"]')
	passwordinput.send_keys(password)
	time.sleep(1)
	passwordbutton = driver.find_element_by_xpath('//*[@id="password-container"]/div[2]/button')
	passwordbutton.click()
	
	time.sleep(1)
	
	nameinput = driver.find_element_by_xpath('//*[@id="login"]')
	nameinput.send_keys(emailname)
	time.sleep(1)
	namebutton = driver.find_element_by_xpath('//*[@id="username-container"]/div[2]/button')
	namebutton.click()
	
	time.sleep(1)
	
	receiveemailinput = driver.find_element_by_xpath('//*[@id="opt_in"]')
	receiveemailinput.send_keys("n")
	time.sleep(1)
	receiveemailbutton = driver.find_element_by_xpath('//*[@id="opt-in-container"]/div[2]/button')
	receiveemailbutton.click()
	print(emailname + emailprefix + ":" + password)

print("created accounts:")
createaccount("nexity453345345", "testaccount123")
