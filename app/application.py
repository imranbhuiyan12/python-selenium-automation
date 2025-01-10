from pages.base_page import Basepage
from pages.cart_page import CartPage
from pages.header import Header
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.search_result_page import SearchResultPage
from pages.side_nav_cart_page import SideNavPage
from pages.sign_in_page import SignINPage
from pages.target_app_page import TargetAppPage
from pages.terms_and_conditions import TermsAndConditions


class Application:


    def __init__(self,driver):
        self.driver = driver
        self.base_page = Basepage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_result_page = SearchResultPage(driver)
        self.cart_page = CartPage(driver)
        self.sign_in_page = SignINPage(driver)
        self.side_nav_cart_page = SideNavPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.privacy_policy_page = PrivacyPolicyPage(driver)
        self.login_page = LoginPage(driver)
        self.terms_and_conditions = TermsAndConditions(driver)





