from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('open the Target Circle page')
def open_circle_page(context):
    context.driver.get('https://www.target.com/circle')

@then('verify there are at least {expected} benefit cells')
def verify_10_cells(context,expected):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/slingshot-components/CellsComponent/Link']")
    print(links)
    assert len(links) == int(expected), f"expected {expected}, found {len(links)}"

