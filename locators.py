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


#find element
driver.find_element(By.ID,"twotabsearchtextbox" )
driver.find_element(By.ID,"nav-search-submit-button" )


#find element, by Xpath
driver.find_element(By.XPATH, "//input[@type='text']")
driver.find_element(By.XPATH, "//input[@tabindex='text']")

#by xpath, any tag buy with attributevalue
driver.find_element(By.XPATH, "//*[@role='searchbox']")