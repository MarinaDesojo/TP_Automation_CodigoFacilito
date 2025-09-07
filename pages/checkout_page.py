# def complete_information_form(self, first_name: str, last_name: str, postal_code: str):
#     self.type(self.INPUT_FIRST_NAME, first_name)
#     self.type(self.INPUT_LAST_NAME, last_name)
#     self.type(self.INPUT_POSTAL_CODE, postal_code)
#     self.click(self.BUTTON_CONTINUE)


from .base_page import BasePage
from selenium.webdriver.common.by import (By)



class Checkout(BasePage):
    LINK_HOMEPAGE = (By.CLASS_NAME, "mr-6 flex items-center space-x-2")
    #BUTTON_CATEGORIES = (By.ID, "radix-«R2bb»-trigger-radix-«Rebb»")
    BUTTON_CATEGORIES = (By.XPATH, '//button[contains(., "Categories")]')
    INPUT_SEARCH = (By.XPATH, '//input') #funciona porque es el unico input tag de la homepage
    LINK_LOGIN = (By.XPATH, '//a[@href="/login"]')
    LINK_SIGNUP = (By.XPATH, '//a[@href="/signup"]')
    LINK_CART = (By.XPATH, '//a[@href="/cart"]')
    SUBMENU_CATEGORIES = (By.XPATH, '//div[@data-orientation="horizontal"]//div[contains(@class, "grid")]')
    LINK_SUBMENU_CATEGORIES = (By.XPATH, '//a[href="/categories/men-clothes" and @data-radix-collection-item]')

    INPUT_FIRST_NAME = (By.ID, "firstName")
    INPUT_LAST_NAME = (By.ID, "lastName")
    INPUT_EMAIL = (By.ID, "email")
    INPUT_PHONE_NUMBER = (By.ID, "phone")
    INPUT_ADDRESS = (By.ID, "address")
    INPUT_CITY = (By.ID, "city")
    INPUT_ZIP_CODE = (By.ID, "zipCode")
    INPUT_COUNTRY = (By.ID, "country")
    LINK_PLACE_ORDER = (By.ID, "place-order-button")
    ORDER_SUMMARY_CARD = (By.ID, "order-summary-card")

    LOADING_OVERLAY = (By.CSS_SELECTOR, 'div.fixed.inset-0.z-50.flex.items-center.justify-center.bg-background\\/70')


    URL = "https://shophub-commerce.vercel.app/checkout" #mejor practica en un archivo de datos modularizado

    def fill_checkout_form(self, first_name: str, last_name: str, email: str, phone_number: str, address: str, city: str, zip_code: str, country: str):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        self.type(self.INPUT_FIRST_NAME, first_name)
        self.type(self.INPUT_LAST_NAME, last_name)
        self.type(self.INPUT_EMAIL, email)
        self.type(self.INPUT_PHONE_NUMBER, phone_number)
        self.type(self.INPUT_ADDRESS, address)
        self.type(self.INPUT_CITY, city)
        self.type(self.INPUT_ZIP_CODE, zip_code)
        self.type(self.INPUT_COUNTRY, country)
        self.click(self.LINK_PLACE_ORDER)