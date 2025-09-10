from .base_page import BasePage
from selenium.webdriver.common.by import (By)
from utils.config import URLS
from utils.config import LOADING_OVERLAY

class SpecialDealsPage(BasePage):
    # Main
    HEADING_CATEGORY_TITLE = (By.ID, "category-title")
    TEXT_CATEGORY_DESCRIPTION = (By.ID, "category-description")

    def load(self):
        self.driver.get(URLS["special_deals"])

    def go_to_cart_page(self):
        self.wait_until_invisible(LOADING_OVERLAY)
        self.click(self.LINK_CART)