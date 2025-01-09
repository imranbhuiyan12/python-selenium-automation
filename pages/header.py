from time import sleep

from pages.base_page import Basepage
from selenium.webdriver.common.by import By


class Header(Basepage):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
    SIGN_IN = (By.XPATH, "//a[@data-test='@web/AccountLink']")
    SIGN_IN_NAV_BAR = (By.XPATH, "//button[@data-test='accountNav-signIn']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='chooseOptionsButton']")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)


    def click_cart(self):
        # self.click(*self.CART_ICON)
        self.wait_and_click(*self.CART_ICON)

    def click_sign_in(self):
        self.click(*self.SIGN_IN)


    def Nav_bar(self):
        self.click(*self.SIGN_IN_NAV_BAR)


    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)



