from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.app.main_page.open_main()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)
    sleep(10)


@when('Click on Cart Icon')
def click_cart(context):
    context.app.header.click_cart()
    sleep(10)

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


@given ('Open target page A-{product_id}')
def open_target_page(context, product_id):
    context.driver.get(f"https://www.target.com/p/A-{product_id}")
    sleep(10)



@then('Search for product {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(10)






