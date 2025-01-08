from pages.base_page import Basepage
from selenium.webdriver.common.by import By
from behave import given, when, then

class SearchResultPage(Basepage):
    SEARCH_RESULT = (By.XPATH, "//div[@data-test='resultsHeading']")


    def verify_search_result(self, product):
        actual_result = self.find_element(*self.SEARCH_RESULT).text
        assert product in actual_result, f'Expected text {product} not in actual {actual_result}'
