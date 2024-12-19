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
driver.maximize_window()

#navigate the target .com
driver.get('https://www.target.com/')


driver.find_element(By.XPATH,"//a[@data-test='@web/AccountLink']").click()
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

sleep(5)

expected = 'Sign into your Target account'
actual = driver.find_element(By.XPATH,"//h1[@class='sc-fe064f5c-0 sc-315b8ab9-2 lnvRvp diHlfH']").text
assert expected == actual, f"{expected} != {actual}"
print("test passed")
driver.find_element(By.ID,'login')
driver.quit()