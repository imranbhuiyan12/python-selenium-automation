from selenium import webdriver
from selenium.webdriver import Keys
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

#find element into the search field
driver.find_element(By.ID,'search').send_keys('tea')
#from search to click
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()


sleep(5)
# verification
expected_result = 'tea'
actual_result = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
assert expected_result in actual_result, f"Expected test {expected_result} not in Actual {actual_result}"

print("test passed")

driver.quit()
