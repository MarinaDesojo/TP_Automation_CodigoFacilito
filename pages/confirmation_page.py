from .base_page import BasePage
from selenium.webdriver.common.by import (By)
from utils.config import URLS
from utils.config import LOADING_OVERLAY

class ConfirmationPage(BasePage):
    # Main
    HEADING_NO_ORDER = (By.XPATH, '//h1[normalize-space()="No Order Found"]')
    TEXT_INFORMATION = (By.XPATH, "//p[normalize-space()='We couldn't find your order information.']")
    LINK_RETURN_HOME= (By.XPATH, '//button[text()="Return to Home"]/ancestor::a')

    def load(self):
        self.driver.get(URLS["confirmation"])

    def return_to_home(self):
        self.wait_until_invisible(LOADING_OVERLAY)
        self.click(self.LINK_RETURN_HOME)