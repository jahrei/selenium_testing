# Import stuff
import selenium
from selenium import webdriver

# Path instantiation
path = "C://Program Files//Google//Chrome//Application//chrome.exe %s"

# Initialize webdriver 
driver = webdriver.Chrome(executable_path=path) 



# Upon launch of script, grab elements from currently open window 
# Reference https://stackoverflow.com/questions/8344776/can-selenium-interact-with-an-existing-browser-session
# Currently unknown if Selenium can interface with already existing browser session

# Extract session_id and _url from driver object
url = driver.command_executor._url
session_id = driver.session_id   

driver = webdriver.Remote(command_executor=url,desired_capabilities={})
driver.close()   # this prevents the dummy browser
driver.session_id = session_id


driver.text("Google Search")


