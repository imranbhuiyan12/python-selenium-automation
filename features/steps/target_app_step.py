from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@given ('Open target app')
def open_target_app(context):
    context.app.target_app_page.open_target_app()



# @then ('Sign in page')
# def open_sign_in_page(context):
#     context.app.target_sign_in_page.open_sign_in_page()





@given ('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window_handle()
    print(context.original_window)



@when ('Click Privacy Policy link')
def click_privacy_policy(context):
    context.app.target_app_page.click_privacy_policy()


@then('Switch to new window')
def switch_window(context):
    # sleep(1)
    # print(f"All window: ", context.driver.window_handles)
    # context.driver.switch_to.window(context.driver.window_handles[1])
    context.app.target_app_page.switch_to_new_window()

@then ('Verify Privacy Policy page opened')
def verify_pp_opened(context):
    context.app.privacy_policy_page.verify_pp_opened()



@then ('Close current page')
def close_page(context):
    context.app.base_page.close()


@then ('Return to original window')
def return_to_original_window(context):
    context.app.privacy_policy_page.switch_to_windows_by_id(context.original_window)






















