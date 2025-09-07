from .base_page import BasePage
from selenium.webdriver.common.by import (By)

class CartPage(BasePage):
    # BUTTON_CHECKOUT = (By.ID, "checkout")
    # INPUT_FIRST_NAME = (By.ID, "first-name")
    # INPUT_LAST_NAME = (By.ID, "last-name")
    # INPUT_POSTAL_CODE = (By.ID, "postal-code")
    # BUTTON_CONTINUE = (By.ID, "continue")
    LINK_HOMEPAGE = (By.CLASS_NAME, "mr-6 flex items-center space-x-2")
    # BUTTON_CATEGORIES = (By.ID, "radix-«R2bb»-trigger-radix-«Rebb»")
    BUTTON_CATEGORIES = (By.XPATH, '//button[contains(., "Categories")]')
    INPUT_SEARCH = (By.XPATH, '//input')  # funciona porque es el unico input tag de la homepage
    LINK_LOGIN = (By.XPATH, '//a[@href="/login"]')
    LINK_SIGNUP = (By.XPATH, '//a[@href="/signup"]')
    LINK_CART = (By.XPATH, '//a[@href="/cart"]')
    SUBMENU_CATEGORIES = (By.XPATH, '//div[@data-orientation="horizontal"]//div[contains(@class, "grid")]')
    LINK_SUBMENU_CATEGORIES = (By.XPATH, '//a[href="/categories/men-clothes" and @data-radix-collection-item]')
    LINK_CHECKOUT = (By.XPATH, '//a[@href="/checkout"]')

    LOADING_OVERLAY = (By.CSS_SELECTOR, 'div.fixed.inset-0.z-50.flex.items-center.justify-center.bg-background\\/70')

    URL = "https://shophub-commerce.vercel.app/cart"

    def go_to_checkout(self):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        self.click(self.LINK_CHECKOUT)

    def complete_information_form(self, first_name: str, last_name: str, postal_code: str):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        self.type(self.INPUT_FIRST_NAME, first_name)
        self.type(self.INPUT_LAST_NAME, last_name)
        self.type(self.INPUT_POSTAL_CODE, postal_code)
        self.click(self.BUTTON_CONTINUE)