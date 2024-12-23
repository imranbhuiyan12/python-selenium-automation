from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then



ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='chooseOptionsButton']")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [data-test='orderPickupButton']")
CONFIRM_BUTTON = (By.CSS_SELECTOR,"[data-test='content-wrapper'] a[href='/cart']")
CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")

# @then('Add product to the cart')
# def add_cart(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='chooseOptionsButton']").click()
#     sleep(10)


@then('Add product to the cart')
def click_add_to_cart(context):
    sleep(2)
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(10)


@then('Product name on sidebar')
def store_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).click()
    sleep(5)




@then('confirm with continue button')
def continue_button(context):
    context.driver.find_element(*CONFIRM_BUTTON).click()
    sleep(5)

@when('Verify cart has {amount} item')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"


@then('Verify search results shown {product}')
def verify_search_results(context, product):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_result, f'Expected text {product} not in actual {actual_result}'