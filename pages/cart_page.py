from .base_page import BasePage
from selenium.webdriver.common.by import (By)

class CartPage(BasePage):
    # URL
    URL = "https://shophub-commerce.vercel.app/cart"  # mejor practica en un archivo de datos modularizado
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
    HEADING_CART = (By.XPATH, '//h1[normalize-space()="Shopping Cart"]')
    # Main - Shopping Cart Information
    TEXT_PRODUCT_NAME = (By.XPATH, '//h3')
    TEXT_PRODUCT_SINGLE_PRICE = (By.CSS_SELECTOR, "p.text-lg.font-bold.text-primary.mt-2")
    TEXT_ORDER_QTY = (By.CSS_SELECTOR, "span.w-12.text-center.font-medium")
    BUTTON_DECREASE_QTY = (By.CSS_SELECTOR, 'button svg.lucide-minus') #no funciona si hay más de un producto diferente
    BUTTON_INCREASE_QTY = (By.CSS_SELECTOR, 'button svg.lucide-plus') #no funciona si hay más de un producto diferente
    BUTTON_REMOVE = (By.CSS_SELECTOR, 'button svg.lucide-trash2') #no funciona si hay más de un producto diferente
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
    HEADING_EMPTY_CART = (By.XPATH, '//h1[normalize-space()="Your Cart is Empty"]')
    TEXT_EMPTY_CART = (By.CLASS_NAME, "mb-8")


    def load(self):
        self.visit(self.URL)

    def go_to_checkout(self):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        self.click(self.LINK_CHECKOUT)

    def decrease_qty(self):
        #self.wait_until_invisible(self.LOADING_OVERLAY)
        svg_icon = self.driver.find_element(*self.BUTTON_DECREASE_QTY)
        button = svg_icon.find_element(By.XPATH, './ancestor::button')
        button.click()

    def increase_qty(self):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        svg_icon = self.driver.find_element(*self.BUTTON_INCREASE_QTY)
        button = svg_icon.find_element(By.XPATH, './ancestor::button')
        button.click()

    def remove_from_cart(self):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        svg_icon = self.driver.find_element(*self.BUTTON_REMOVE)
        button = svg_icon.find_element(By.XPATH, './ancestor::button')
        button.click()

    def continue_shopping(self):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        self.click(self.LINK_CONTINUE_SHOPPING)