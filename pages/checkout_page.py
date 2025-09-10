from .base_page import BasePage
from selenium.webdriver.common.by import (By)
from utils.config import URLS
from utils.config import LOADING_OVERLAY

class CheckoutPage(BasePage):
    # Main
    HEADING_CHECKOUT = (By.ID, "checkout-page-title")
    # Main - Customer Information Form
    HEADING_CUSTOMER_INFORMATION = (By.ID, "customer-info-title")
    INPUT_FIRST_NAME = (By.ID, "firstName")
    INPUT_LAST_NAME = (By.ID, "lastName")
    INPUT_EMAIL = (By.ID, "email")
    INPUT_PHONE_NUMBER = (By.ID, "phone")
    INPUT_ADDRESS = (By.ID, "address")
    INPUT_CITY = (By.ID, "city")
    INPUT_ZIP_CODE = (By.ID, "zipCode")
    INPUT_COUNTRY = (By.ID, "country")
    LINK_PLACE_ORDER = (By.ID, "place-order-button")
    # Main - Order summary
    HEADING_ORDER_SUMMARY = (By.ID, "order-summary-card")
    TEXT_PRODUCT_NAME = (By.ID, "order-item-name-24")
    TEXT_ORDER_QTY = (By.ID, "order-item-qty-24")
    TEXT_SUBTOTAL_PRODUCT_PRICE = (By.ID, "subtotal-row")
    TEXT_SUBTOTAL_SHIPPING_PRICE = (By.ID, "shipping-row")
    TEXT_SUBTOTAL_TAX_PRICE = (By.ID, "tax-row")
    TEXT_TOTAL_PRICE = (By.ID, "total-row")

    def load(self):
        self.driver.get(URLS["checkout"])

    def fill_checkout_form(self, first_name: str, last_name: str, email: str, phone_number: str, address: str, city: str, zip_code: str, country: str):
        self.wait_until_invisible(LOADING_OVERLAY)
        self.type(self.INPUT_FIRST_NAME, first_name)
        self.type(self.INPUT_LAST_NAME, last_name)
        self.type(self.INPUT_EMAIL, email)
        self.type(self.INPUT_PHONE_NUMBER, phone_number)
        self.type(self.INPUT_ADDRESS, address)
        self.type(self.INPUT_CITY, city)
        self.type(self.INPUT_ZIP_CODE, zip_code)
        self.type(self.INPUT_COUNTRY, country)
        self.click(self.LINK_PLACE_ORDER)