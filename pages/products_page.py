from .base_page import BasePage
from selenium.webdriver.common.by import (By)

class ProductPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "title")
    CART_BADGE = (By.CSS_SELECTOR, "shopping-cart-badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_by_name(self, product_name:str):
        add_button = (By.XPATH, f"//button[@id='add-to-cart-{product_name}']")
        self.click(add_button)

    def go_to_shopping_cart(self):
        self.click(self.CART_LINK)