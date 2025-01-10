from time import sleep

from pages.base_page import Basepage
from selenium.webdriver.common.by import By


class TermsAndConditions(Basepage):



    def verify_terms_conditions_page(self):
        self.verify_partial_url('terms-conditions')
