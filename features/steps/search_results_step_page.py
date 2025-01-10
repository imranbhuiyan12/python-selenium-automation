from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC



# ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='chooseOptionsButton']")
# PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [data-test='orderPickupButton']")
# CONFIRM_BUTTON = (By.CSS_SELECTOR,"[data-test='content-wrapper'] a[href='/cart']")
# CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
# STORE_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
VERIFY_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
COLOR_OPTION = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
COLOR_SELECT = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")
LISTING = (By.CSS_SELECTOR, "[data-test*='@web/site-top-of-funnel/ProductCardWrapper']")
TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
IMAGE = (By.CSS_SELECTOR, 'img')

# @then('Add product to the cart')
# def add_cart(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='chooseOptionsButton']").click()
#     sleep(10)


@then('Add product to the cart')
def click_add_to_cart(context):
    sleep(2)
    # context.driver.find_element(*ADD_TO_CART_BTN).click()
    # # context.driver.wait.until(EC.visibility_of_element_located(*ADD_TO_CART_BTN))
    context.app.header.click_add_to_cart()


@then('Product name on sidebar')
def store_product_name(context):
    # context.product_name = context.driver.find_element(*PRODUCT_NAME).click()
    # sleep(5)
    context.app.cart_page.store_product_name()

@then('Store product name')
def product_name(context):
    # context.product = context.driver.find_element(*STORE_PRODUCT_NAME).text
    # print(f"Product name: {context.product}")
    # context.app.cart_page.product_name()
    context.product_name = context.app.search_result_page.get_product_name()
    print(f'Product stored: {context.product_name}')



@then('confirm with continue button')
def continue_button(context):
    # context.driver.find_element(*CONFIRM_BUTTON).click()
    # sleep(5)
    context.app.side_nav_cart_page.continue_button()

@when('Verify cart has {amount} item')
def verify_cart_items(context, amount):
    # cart_summary = context.driver.find_element(*CART_SUMMARY).text
    # assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"
    context.app.cart_page.verify_cart_items(amount)


@then('Verify product name')
def verify_product(context):
    # actual_name = context.driver.find_element(*VERIFY_PRODUCT_NAME).text
    # print(f"Product name: {actual_name}")
    # print(f"Product name stored earlier:{context.product}")
    # assert context.product in actual_name, f"Expected {context.product } but got {actual_name}"
    # context.app.cart_page.verify_product(context.product)
    context.app.cart_page.verify_product(context.product_name)



@then('Verify search results shown {product}')
def verify_search_results(context, product):
    context.app.search_result_page.verify_search_result(product)


@then ('verify search term {product} in URL')
def verify_search_url(context, product):
    context.app.search_result_page.verify_search_url(product)

#cart features

@then('Verify “Your cart is empty” message is shown')
def verify_cart(context):
    context.app.cart_page.verify_cart()

#-------------------------------------------------------------------------------

#Sign in form
@then('Verify Sign In form opened')
def verify_sign_in(context):
    # expected = 'Sign into your Target account'
    # actual = context.driver.find_element(By.XPATH, "//h1[@class='sc-fe064f5c-0 sc-315b8ab9-2 lnvRvp diHlfH']").text
    # assert expected == actual, f"{expected} not in  {actual}"
    # print("test passed")
    context.app.sign_in_page.verify_sign_in()




#----------------------------------------------

@then('Verify that color selected by user')
def verify_color(context):
    expected_color = ['Blue Tint', 'Denim Blue', 'Raven', 'Marine']
    actual_color = []

    colors = context.driver.find_elements(*COLOR_OPTION)
    print(colors)

    for color in colors:
        print(color)
        color.click()
        selected_color = context.driver.find_element(*COLOR_SELECT).text
        print("Current color:", selected_color )
        selected_color = selected_color.split('\n')[1]
        actual_color.append(selected_color)
        print("actual_color:", actual_color)

    assert actual_color == expected_color, f"expected {expected_color} did not match actual {actual_color} colors"






@then('Verify product name and image')
def verify_product_name_image(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_products = context.driver.find_elements(*LISTING)
    print("all products name:", all_products)
    assert len(all_products) > 0, 'No products found'
    for product in all_products:
        title = context.driver.find_element(*TITLE).text
        assert title != '', f"product not shown"
        print(title)
        product.find_element(*IMAGE)


