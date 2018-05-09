import os
import selenium
from selenium import webdriver

# setting up google chrome as a web browser for tests

chromedriver = os.path.dirname(os.path.abspath(__file__)) + "/chrome/chromedriver" # chrome driver binary

os.environ["webdriver.chrome.driver"] = chromedriver

Config = {
	"chromedriver":chromedriver, 

	"siteurl":"http://google.com",
	
	"log_filename":"logs/logfilename.log",

	"screenshot_store":"store/"
}
