from selenium import webdriver
from selenium.webdriver.common.keys import Keys

emailname = "randomtestaccountBTUITERSBI"
driver = webdriver.Firefox()
driver.get("https://github.com/signup?user_email=" + emailname + "%40planecrazyarchive.tk&source=form-home-signup")
wait(10)
emailbutton = driver.find_element_by_xpath('//*[@id="email-container"]/div[2]/button')
emailbutton.click()
wait(3)

passwordinput = driver.find_element_by_xpath('//*[@id="password"]')
passwordinput.send_keys("testpasswordTETBWETWBTEW$T")
wait(3)
passwordbutton = driver.find_element_by_xpath('//*[@id="password-container"]/div[2]/button')
passwordbutton.click()

wait(3)

nameinput = driver.find_element_by_xpath('//*[@id="login"]')
nameinput.send_keys(emailname)
wait(3)
namebutton = driver.find_element_by_xpath('//*[@id="username-container"]/div[2]/button')
namebutton.click()

wait(3)

receiveemailinput = driver.find_element_by_xpath('//*[@id="opt_in"]')
receiveemailinput.send_keys("n")
wait(3)
receiveemailbutton = driver.find_element_by_xpath('//*[@id="opt-in-container"]/div[2]/button')
receiveemailbutton.click()
