from pages.base_page import Basepage
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_result_page import SearchResultPage

class Application:


    def __init__(self,driver):
        self.driver = driver
        self.base_page = Basepage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_result_page = SearchResultPage(driver)
        self.cart_page = CartPage(driver)




