from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get("https://target.com/")

@when('Search for {search_word}')
def search_product(context, search_word):
    context.driver.find_element(By.ID, 'search').send_keys(search_word)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(10)


@when('Click on Cart Icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/CartIcon']").text()

@then('Verify header links are shown')
def verify_header_links(context):
    el = context.driver.find_element(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print('\nFind element:')
    print(el)



@then('Verify {expected_amount} header links are shown')
def verify_header_links_amount(context, expected_amount):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print('\nFind elements:')
    print(links)
    print(type(len(links)))

    assert len(links) == int(expected_amount), f'Expected {expected_amount} links but got {len(links)}'



# @then('Search for mug')
# def search_product(context):
#     context.driver.find_element(By.ID, 'search').send_keys('mug')
#     context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/Search/SearchButton']").click()
#     sleep(5)






