from pages.base_page import Basepage
from selenium.webdriver.common.by import By



class CartPage(Basepage):
    CART_EMPTY = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def verify_cart(self):
        expected_result = 'Your cart is empty'
        actual_result = self.driver.find_element(*self.CART_EMPTY).text
        assert expected_result == actual_result, f"expected {expected_result} did not match {actual_result}"
        print("test passed")


