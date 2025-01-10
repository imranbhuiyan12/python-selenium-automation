from time import sleep

from pages.base_page import Basepage
from selenium.webdriver.common.by import By


class MainPage(Basepage):

    LOGIN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    LOGIN_SIDE_BAR = (By. CSS_SELECTOR, "[data-test='accountNav-signIn']")


    def open_main(self):
        self.open_url("https://target.com/")




    def click_login(self):
        self.click(*self.LOGIN)



    def login_side_bar(self):
        self.click(*self.LOGIN_SIDE_BAR)
        sleep(5)



