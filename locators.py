from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)


#find element by ID
driver.find_element(By.ID, 'twotabsearchtextbox' )
driver.find_element(By.ID, 'nav-search-submit-button' )

#find element by XPATH
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
driver.find_element(By.XPATH, "//input[@role='searchbox']")

#find element by XPATH with any tag
driver.find_element(By.XPATH, "//*[@role='searchbox']")
#find element by XPATH with multiple attribute
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon' and  @type='text']")
#find element by XPATH with text

driver.find_element(By.XPATH, "//a[text()='Same-Day Delivery' and @class='nav-a  ']")
driver.find_element(By.XPATH, "//a[text()='Same-Day Delivery']")