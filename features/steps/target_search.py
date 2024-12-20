from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep













@then('Click sign in button')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()

@when('Nav bar sign button')
def Nav_bar(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

@then('Verify Sign In form opened')
def verify_sign_in(context):
    expected = 'Sign into your Target account'
    actual = context.driver.find_element(By.XPATH, "//h1[@class='sc-fe064f5c-0 sc-315b8ab9-2 lnvRvp diHlfH']").text
    assert expected == actual, f"{expected} not in  {actual}"
    print("test passed")


