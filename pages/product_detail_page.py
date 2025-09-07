from .base_page import BasePage
from selenium.webdriver.common.by import (By)



class PDP(BasePage):
    LINK_HOMEPAGE = (By.CLASS_NAME, "mr-6 flex items-center space-x-2")
    #BUTTON_CATEGORIES = (By.ID, "radix-«R2bb»-trigger-radix-«Rebb»")
    BUTTON_CATEGORIES = (By.XPATH, '//button[contains(., "Categories")]')
    INPUT_SEARCH = (By.XPATH, '//input') #funciona porque es el unico input tag de la homepage
    LINK_LOGIN = (By.XPATH, '//a[@href="/login"]')
    LINK_SIGNUP = (By.XPATH, '//a[@href="/signup"]')
    LINK_CART = (By.XPATH, '//a[@href="/cart"]')
    SUBMENU_CATEGORIES = (By.XPATH, '//div[@data-orientation="horizontal"]//div[contains(@class, "grid")]')
    LINK_SUBMENU_CATEGORIES = (By.XPATH, '//a[href="/categories/men-clothes" and @data-radix-collection-item]')
    LINK_BACK_TO_CATEGORY_ELECTRONICS = (By.ID, "back-btn-24")
    BUTTON_ADD_TO_QTY = (By.ID, "quantity-increase-24")
    BUTTON_ADD_TO_CART = (By.ID, "add-to-cart-main-24")

    LOADING_OVERLAY = (By.CSS_SELECTOR, 'div.fixed.inset-0.z-50.flex.items-center.justify-center.bg-background\\/70')

    URL = "https://shophub-commerce.vercel.app/product/24" #mejor practica en un archivo de datos modularizado

    def add_product_qty(self):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        self.click(self.BUTTON_ADD_TO_QTY)

    def add_product_to_cart(self):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        self.click(self.BUTTON_ADD_TO_CART)

    def go_to_cart_page(self):
        self.click(self.LINK_CART)
