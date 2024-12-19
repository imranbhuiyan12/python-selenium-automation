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

driver.find_element(By.CSS_SELECTOR, ".a-link-nav-icon")
driver.find_element(By.ID, "ap_customer_name")
driver.find_element(By.ID, "ap_email")
driver.find_element(By.ID, "ap_password")
driver.find_element(By.ID, "ap_password_check")
driver.find_element(By.CSS_SELECTOR,"input.a-button-input")
driver.find_element(By.CSS_SELECTOR, "[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")