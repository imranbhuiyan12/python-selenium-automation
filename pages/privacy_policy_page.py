from time import sleep

from pages.base_page import Basepage
from selenium.webdriver.common.by import By


class PrivacyPolicyPage(Basepage):
    def verify_pp_opened(self):
        self.verify_partial_url('target-privacy-policy')





