from time import sleep

from pages.base_page import Basepage
from selenium.webdriver.common.by import By


class TargetAppPage(Basepage):

    PP_LINK = (By.CSS_SELECTOR, "[aria-label='privacy policy - opens in a new window']")

    def open_target_app(self):
        self.open_url("https://www.target.com/c/target-app")


    def click_privacy_policy(self):
        self.click(*self.PP_LINK)
        sleep(5)

    # def switch_to_new_window(self):



