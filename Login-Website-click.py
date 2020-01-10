import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# create a new Chrome session
browser = webdriver.Chrome()

# Navigate to the application home page
browser.get('https://confluence.abc.com/login.action')



#Login

time.sleep(3)
username = browser.find_element_by_id("os_username")
password = browser.find_element_by_id("os_password")

username.send_keys("ssreedha")

password.send_keys("Hamsi@321")

login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()


# get the search textbox

#search = browser.find_element_by_id('SharedDocumentation-Searchthisdocumentation')
search = browser.find_element_by_name('queryString')


search.send_keys("Satellite Core Team Home")

search.send_keys(Keys.RETURN)

#browser.switchTo().window(tabs.get(1)); #switches to new tab
browser.get("https://confluence.abc.com/display/AEPS/Application+Engineering+Onboarding")
time.sleep(3)

#To click on a link
link = browser.find_element_by_link_text('TeamCity')
link.click()


#wait for 3 seconds 
time.sleep(3)

#Login to this new url

username1 = browser.find_element_by_id("username")
password1 = browser.find_element_by_id("password")



username1.send_keys("user")

password1.send_keys("password")

login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()


#wait for 3 seconds 
time.sleep(3)

browser.get("http://teamcity.abc.com/project.html?projectId=FpChannel")


#browser.quit()
#browser.findElement(By.linkText("Blog"));
#browser.findElement(By.linkText("TeamCity")).Click()
#browser.FindElement(By.Id("my-id")).Click();


# hit return after you enter search text
#time.sleep(25) # sleep for 5 seconds so you can see the results
#browser.quit()



