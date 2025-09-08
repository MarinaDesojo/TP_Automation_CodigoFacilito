from .base_page import BasePage
from selenium.webdriver.common.by import (By)



class ProductPage(BasePage):
    # URL
    URL = "https://shophub-commerce.vercel.app/product/"  # mejor practica en un archivo de datos modularizado
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
    HEADING_CATEGORY_TITLE = (By.ID, "product-main-title-24")
    TEXT_CATEGORY_DESCRIPTION = (By.ID, "product-category-24")
    TEXT_PRODUCT_PRICE = (By.ID, "product-main-price-24")
    TEXT_PRODUCT_DESCRIPTION_TITLE = (By.ID, "product-desc-title-24")
    TEXT_PRODUCT_DESCRIPTION = (By.ID, "product-desc-text-24")
    TEXT_QTY = (By.ID, "quantity-display-24")
    CONTAINER_PRODUCT_FEATURES = (By.ID, "product-features-24")
    TEXT_FEATURE_SHIPPING = (By.ID, "feature-shipping-24")
    TEXT_FEATURE_RETURN = (By.ID, "feature-returns-24")
    TEXT_FEATURE_PAYMENT = (By.ID, "feature-payment-24")

    def load(self, product_number):
        product_url = self.URL + f"/{product_number}"
        self.visit(self.product_url)

    def go_to_cart_page(self):
        self.click(self.LINK_CART)

    # def increase_product_qty(self):
    #     self.wait_until_invisible(self.LOADING_OVERLAY)
    #     self.click(self.BUTTON_INCREASE_QTY)
    #
    # def add_product_to_cart(self):
    #     self.wait_until_invisible(self.LOADING_OVERLAY)
    #     self.click(self.BUTTON_ADD_TO_CART)

    def increase_product_qty(self, product_number: str):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        if not product_number.isdigit() or not (1 <= int(product_number) <= 50):
            raise ValueError("product_number debe estar entre '1' y '50'")
        increase = (By.ID, f"quantity-increase-{product_number}")
        self.click(increase)

    def decrease_product_qty(self, product_number: str):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        if not product_number.isdigit() or not (1 <= int(product_number) <= 50):
            raise ValueError("product_number debe estar entre '1' y '50'")
        decrease = (By.ID, f"quantity-decrease-{product_number}")
        self.click(decrease)

    def add_to_cart(self, product_number: str):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        if not product_number.isdigit() or not (1 <= int(product_number) <= 50):
            raise ValueError("product_number debe estar entre '1' y '50'")
        add_to_cart = (By.ID, f"add-to-cart-main-{product_number}")
        self.click(add_to_cart)

    def go_back_to_category(self, product_number: str):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        if not product_number.isdigit() or not (1 <= int(product_number) <= 50):
            raise ValueError("product_number debe estar entre '1' y '50'")
        back = (By.ID, f"back-btn-{product_number}")
        self.click(back)

    def mark_as_favorite(self, product_number: str):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        if not product_number.isdigit() or not (1 <= int(product_number) <= 50):
            raise ValueError("product_number debe estar entre '1' y '50'")
        fav = (By.ID, f"wishlist-{product_number}")
        self.click(fav)


