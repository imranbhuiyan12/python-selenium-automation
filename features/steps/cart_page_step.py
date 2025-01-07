from selenium.webdriver.common.by import By
from behave import given, when, then



@then('Verify “Your cart is empty” message is shown')
def verify_cart(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR,"[data-test='boxEmptyMsg']").text
    assert expected_result == actual_result, f"expected {expected_result} in Actual {actual_result}"
    print("test passed")



