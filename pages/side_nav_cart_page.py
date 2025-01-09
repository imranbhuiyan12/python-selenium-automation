from time import sleep

from pages.base_page import Basepage
from selenium.webdriver.common.by import By



class SideNavPage(Basepage):
    CONFIRM_BUTTON = (By.CSS_SELECTOR,"[data-test='content-wrapper'] a[href='/cart']")





    def continue_button(self):
        self.click(*self.CONFIRM_BUTTON)
        sleep(5)