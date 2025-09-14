from .base_page import BasePage
from selenium.webdriver.common.by import (By)
from utils.config import URLS
from utils.config import LOADING_OVERLAY

class CartPage(BasePage):
    # Locators
    # Main
    HEADING_CART = (By.XPATH, '//h1[normalize-space()="Shopping Cart"]')
    # Main - Shopping Cart Information
    TEXT_PRODUCT_NAME = (By.XPATH, '//h3')
    TEXT_PRODUCT_SINGLE_PRICE = (By.CSS_SELECTOR, "p.text-lg.font-bold.text-primary.mt-2")
    TEXT_ORDER_QTY = (By.CSS_SELECTOR, "span.w-12.text-center.font-medium")
    SVG_DECREASE_QTY = (By.CSS_SELECTOR, 'button svg.lucide-minus')
    SVG_INCREASE_QTY = (By.CSS_SELECTOR, 'button svg.lucide-plus')
    SVG_REMOVE = (By.CSS_SELECTOR, 'button svg.lucide-trash2')
    BUTTON_CONTAINER = (By.XPATH, "./ancestor::button")
    TEXT_PRODUCT_TOTAL_PRICE = (By.CLASS_NAME, "text-right")
    # Main - Order summary
    HEADING_ORDER_SUMMARY = (By.XPATH, '//div[normalize-space()="Order Summary"]')
    #TEXT_SUBTOTAL_PRODUCT_PRICE =
    #TEXT_SUBTOTAL_SHIPPING_PRICE =
    #TEXT_SUBTOTAL_TAX_PRICE =
    #TEXT_TOTAL_PRICE =
    LINK_CHECKOUT = (By.XPATH, '//a[@href="/checkout"]')
    LINK_CONTINUE_SHOPPING = (By.XPATH, '//a[@href="/" and .//button[normalize-space(text())="Continue Shopping"]]')
    # Empty cart
    HEADING_EMPTY_CART = (By.TAG_NAME, "h1")
    TEXT_EMPTY_CART = (By.CLASS_NAME, "mb-8")

    # Content
    HEADING = "Shopping Cart"
    # Content Empty Cart
    HEADING_EMPTY = "Your Cart is Empty"
    TEXT = "Looks like you haven't added any items to your cart yet."
    LINK_TEXT = "Continue Shopping"

    def load(self):
        self.driver.get(URLS["cart"])
        self.assert_url("cart")
        self.wait_until_invisible(LOADING_OVERLAY)

    def go_to_checkout(self):
        self.click(self.LINK_CHECKOUT)
        self.assert_url("checkout")
        self.wait_until_invisible(LOADING_OVERLAY)

    def _get_product_card(self, product_name):
        return self.driver.find_element(By.XPATH, f"//div[@class='p-6'][.//h3[text()='{product_name}']]")

    def decrease_qty(self, product_name):
        card = self._get_product_card(product_name)
        svg_icon = card.find_element(*self.SVG_DECREASE_QTY)
        button = svg_icon.find_element(*self.BUTTON_CONTAINER)
        button.click()

    def increase_qty(self, product_name):
        card = self._get_product_card(product_name)
        svg_icon = card.find_element(*self.SVG_INCREASE_QTY)
        button = svg_icon.find_element(*self.BUTTON_CONTAINER)
        button.click()

    def remove_from_cart(self, product_name):
        card = self._get_product_card(product_name)
        svg_icon = card.find_element(*self.SVG_REMOVE)
        button = svg_icon.find_element(*self.BUTTON_CONTAINER)
        button.click()

    def continue_shopping(self):
        self.click(self.LINK_CONTINUE_SHOPPING)
        self.assert_url("homepage")
        self.wait_until_invisible(LOADING_OVERLAY)

    def cart_empty_verification(self):
        self.verify_element_removed_and_empty_state_displayed(
        removed_locator = self.SVG_REMOVE,
        expected_locator = self.HEADING_EMPTY_CART)

    def verify_cart_empty_text(self):
        self.assert_text_of_element(locator=self.HEADING_EMPTY_CART, expected_text=self.HEADING_EMPTY)

