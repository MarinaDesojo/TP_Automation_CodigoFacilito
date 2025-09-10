from .base_page import BasePage
from selenium.webdriver.common.by import (By)
from utils.config import URLS
from utils.config import LOADING_OVERLAY

class ElectronicsPage(BasePage):
    # Main
    HEADING_CATEGORY_TITLE = (By.ID, "category-title")
    TEXT_CATEGORY_DESCRIPTION = (By.ID, "category-description")

    def load(self):
        self.driver.get(URLS["electronics"])

    def go_to_cart_page(self):
        self.wait_until_invisible(LOADING_OVERLAY)
        self.click(self.LINK_CART)

    def go_to_product_page_by_number_21_30(self, product_number: str):
        self.wait_until_invisible(LOADING_OVERLAY)
        if not product_number.isdigit() or not (21 <= int(product_number) <= 30):
            raise ValueError("product_number has to be between '21' and '30'")
        product_detail_link = (By.CSS_SELECTOR, f'[href="/product/{product_number}"]')
        self.click(product_detail_link)

    def add_product_to_cart_by_number_21_30(self, product_number: str):
        self.wait_until_invisible(LOADING_OVERLAY)
        if not product_number.isdigit() or not (21 <= int(product_number) <= 30):
            raise ValueError("product_number has to be between '21' and '30'")
        add_button = (By.ID, f"add-to-cart-{product_number}")
        self.click(add_button)