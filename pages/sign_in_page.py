
from pages.base_page import Basepage
from selenium.webdriver.common.by import By


class SignINPage(Basepage):
    SIGN_IN_PAGE = (By.XPATH, "//h1[@class='sc-fe064f5c-0 sc-315b8ab9-2 lnvRvp diHlfH']")


    def verify_sign_in(self):
        expected_text = 'Sign into your Target account'
        actual_text = self.driver.find_element(*self.SIGN_IN_PAGE).text
        assert expected_text == actual_text, f"{expected_text} not in  {actual_text}"