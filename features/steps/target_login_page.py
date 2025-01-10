from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@then ('Open target main page')
def open_main(context):
    context.app.main_page.open_main()


@then ('Click on login')
def click_login(context):
    # context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    context.app.main_page.click_login()


@then ('Click login from side bar')
def login_side_bar(context):
    context.app.main_page.login_side_bar()


@then ('Store original window')
def store_current_window(context):
    context.original = context.app.base_page.get_current_window_handle()
    print(context.original)


@then('Click on Target terms and conditions link')
def click_terms_conditions(context):
    # context.driver.find_element(By.CSS_SELECTOR, "[aria-label='terms & conditions - opens in a new window']").click()
    context.app.login_page.click_terms_conditions()


@then('switch to the newly opened window')
def switch_new_page(context):
    context.app.base_page.switch_to_new_window()

@then ('Verify Terms and Conditions page is opened')
def verify_terms_conditions_page(context):
    context.app.terms_and_conditions.verify_terms_conditions_page()


@then ('User can close new window')
def close_new_window(context):
    context.app.base_page.close()

@then ('Return to login window')
def return_to_login_window(context):
    context.app.base_page.switch_to_windows_by_id(context.original)



