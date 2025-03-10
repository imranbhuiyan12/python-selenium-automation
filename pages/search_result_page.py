from pages.base_page import Basepage
from selenium.webdriver.common.by import By


class SearchResultPage(Basepage):
    SEARCH_RESULT = (By.XPATH, "//div[@data-test='resultsHeading']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")

    def verify_search_result(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULT)


    def verify_search_url(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULT)

    def get_product_name(self):
        return self.find_element(*self.PRODUCT_NAME).text
