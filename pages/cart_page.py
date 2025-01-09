from time import sleep

from pages.base_page import Basepage
from selenium.webdriver.common.by import By



class CartPage(Basepage):
    CART_EMPTY = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [data-test='orderPickupButton']")
    CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")



    def verify_cart(self):
        expected_result = 'Your cart is empty'
        self.verify_text(expected_result, *self.CART_EMPTY)
        print("test passed")


    def store_product_name(self):
        self.click(*self.PRODUCT_NAME)
        sleep(10)


    def verify_cart_items(self, amount):
        cart_summary = self.driver.find_element(*self.CART_SUMMARY).text
        assert amount in cart_summary, f"Expected {amount} items but got {cart_summary}"





