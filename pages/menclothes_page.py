from .base_page import BasePage
from selenium.webdriver.common.by import (By)

class MenClothesPage(BasePage):
    # URL
    URL = "https://shophub-commerce.vercel.app/categories/men-clothes"  # mejor practica en un archivo de datos modularizado
    # Header
    LINK_HOMEPAGE = (By.CSS_SELECTOR, "a.mr-6.flex.items-center.space-x-2")
    BUTTON_CATEGORIES = (By.XPATH, '//button[contains(., "Categories")]')
    INPUT_SEARCH = (By.XPATH, '//input[@placeholder="Search products..."]')
    LINK_LOGIN = (By.XPATH, '//a[@href="/login"]')
    LINK_SIGNUP = (By.XPATH, '//a[@href="/signup"]')
    LINK_CART = (By.XPATH, '//a[@href="/cart"]')
    # Overlay
    LOADING_OVERLAY = (By.CSS_SELECTOR, 'div.fixed.inset-0.z-50.flex.items-center.justify-center.bg-background\\/70')
    # Main
    HEADING_CATEGORY_TITLE = (By.ID, "category-title")
    TEXT_CATEGORY_DESCRIPTION = (By.ID, "category-description")

    def load(self):
        self.visit(self.URL)

    def go_to_cart_page(self):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        self.click(self.LINK_CART)

    def go_to_product_page_by_number(self, product_number: str):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        if not product_number.isdigit() or not (1 <= int(product_number) <= 10):
            raise ValueError("product_number debe estar entre '1' y '10'")
        product_detail_link = (By.CSS_SELECTOR, f'[href="/product/{product_number}"]')
        self.click(product_detail_link)

    def add_product_to_cart_by_number(self, product_number: str):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        if not product_number.isdigit() or not (1 <= int(product_number) <= 10):
            raise ValueError("product_number debe estar entre '1' y '10'")
        add_button = (By.ID, f"add-to-cart-{product_number}")
        self.click(add_button)