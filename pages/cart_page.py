from time import sleep

from pages.base_page import Basepage
from selenium.webdriver.common.by import By



class CartPage(Basepage):
    CART_EMPTY = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
    CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
    VERIFY_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")




    def verify_cart(self):
        expected_result = 'Your cart is empty'
        self.verify_text(expected_result, *self.CART_EMPTY)
        print("test passed")


    def store_product_name(self):
        self.click(*self.PRODUCT_NAME)
        sleep(5)


    def verify_cart_items(self, amount):
        cart_summary = self.driver.find_element(*self.CART_SUMMARY).text
        assert amount in cart_summary, f"Expected {amount} items but got {cart_summary}"


    def verify_product(self,expected_text):
        self.verify_partial_text(expected_text, *self.VERIFY_PRODUCT_NAME)
        print(expected_text)






