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

driver.find_element(By.ID,'ap_email')
driver.find_element(By.ID,'continue')
driver.find_element(By.ID,'auth-fpp-link-bottom')
driver.find_element(By.ID,'ap-other-signin-issues-link')
driver.find_element(By.ID,'createAccountSubmit')
#find element by XPATH

driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']")
driver.find_element(By.XPATH, "//h5[text()='New to Amazon?']")
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

