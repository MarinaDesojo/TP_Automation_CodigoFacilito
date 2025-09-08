from .base_page import BasePage
from selenium.webdriver.common.by import (By)

class ElectronicsPage(BasePage):
    # URL
    URL = "https://shophub-commerce.vercel.app/categories/electronics"  # mejor practica en un archivo de datos modularizado
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
    # LINK_PRODUCT_PAGE_21 = (By.CSS_SELECTOR, '[href="/product/21"]')
    # LINK_PRODUCT_PAGE_22 = (By.CSS_SELECTOR, '[href="/product/22"]')
    # LINK_PRODUCT_PAGE_23 = (By.CSS_SELECTOR, '[href="/product/23"]')
    # LINK_PRODUCT_PAGE_24 = (By.CSS_SELECTOR, '[href="/product/24"]')
    # LINK_PRODUCT_PAGE_25 = (By.CSS_SELECTOR, '[href="/product/25"]')
    # LINK_PRODUCT_PAGE_26 = (By.CSS_SELECTOR, '[href="/product/26"]')
    # LINK_PRODUCT_PAGE_27 = (By.CSS_SELECTOR, '[href="/product/27"]')
    # LINK_PRODUCT_PAGE_28 = (By.CSS_SELECTOR, '[href="/product/28"]')
    # LINK_PRODUCT_PAGE_29 = (By.CSS_SELECTOR, '[href="/product/29"]')
    # LINK_PRODUCT_PAGE_30 = (By.CSS_SELECTOR, '[href="/product/30"]')
    # BUTTON_ADD_TO_CART_21 = (By.ID, "add-to-cart-21")
    # BUTTON_ADD_TO_CART_22 = (By.ID, "add-to-cart-22")
    # BUTTON_ADD_TO_CART_23 = (By.ID, "add-to-cart-23")
    # BUTTON_ADD_TO_CART_24 = (By.ID, "add-to-cart-24")
    # BUTTON_ADD_TO_CART_25 = (By.ID, "add-to-cart-25")
    # BUTTON_ADD_TO_CART_26 = (By.ID, "add-to-cart-26")
    # BUTTON_ADD_TO_CART_27 = (By.ID, "add-to-cart-27")
    # BUTTON_ADD_TO_CART_28 = (By.ID, "add-to-cart-28")
    # BUTTON_ADD_TO_CART_29 = (By.ID, "add-to-cart-29")
    # BUTTON_ADD_TO_CART_30 = (By.ID, "add-to-cart-30")

    def load(self):
        self.visit(self.URL)

    def go_to_cart_page(self):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        self.click(self.LINK_CART)

    # def go_to_product_page_23(self):
    #     self.wait_until_invisible(self.LOADING_OVERLAY)
    #     self.click(self.LINK_PRODUCT_PAGE_23)
    #
    # def go_to_product_page_24(self):
    #     self.wait_until_invisible(self.LOADING_OVERLAY)
    #     self.click(self.LINK_PRODUCT_PAGE_24)

    # def add_product_to_cart_23(self):
    #     self.wait_until_invisible(self.LOADING_OVERLAY)
    #     self.click(self.BUTTON_ADD_TO_CART_23)
    #
    # def add_product_to_cart_24(self):
    #     self.wait_until_invisible(self.LOADING_OVERLAY)
    #     self.click(self.BUTTON_ADD_TO_CART_24)

    def go_to_product_page_by_number(self, product_number: str):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        if not product_number.isdigit() or not (21 <= int(product_number) <= 30):
            raise ValueError("product_number debe estar entre '21' y '30'")
        product_detail_link = (By.CSS_SELECTOR, f'[href="/product/{product_number}"]')
        self.click(product_detail_link)

    def add_product_to_cart_by_number(self, product_number: str):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        if not product_number.isdigit() or not (21 <= int(product_number) <= 30):
            raise ValueError("product_number debe estar entre '21' y '30'")
        add_button = (By.ID, f"add-to-cart-{product_number}")
        self.click(add_button)