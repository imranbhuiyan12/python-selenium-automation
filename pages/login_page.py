from time import sleep

from pages.base_page import Basepage
from selenium.webdriver.common.by import By



class LoginPage(Basepage):
    TANDC = (By.CSS_SELECTOR, "[aria-label='terms & conditions - opens in a new window']")

    def click_terms_conditions(self):
        self.click(*self.TANDC)