from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_main(context):
    context.driver.get("https://target.com/")

@when('Search for tea')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)

@when('Search for paste')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('paste')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)

@then('Verify search results shown')
def verify_search(context):
    expected_result = 'tea'
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_result in actual_result, f"Expected test {expected_result} not in Actual {actual_result}"
    print("test passed")


@when('Click on Cart Icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/CartIcon']").click()
    sleep(5)

@then('Verify “Your cart is empty” message is shown')
def verify_cart(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR,"[data-test='boxEmptyMsg']").text
    assert expected_result == actual_result, f"expected {expected_result} in Actual {actual_result}"
    print("test passed")


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


