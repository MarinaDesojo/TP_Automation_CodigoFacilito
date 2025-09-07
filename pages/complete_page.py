from .base_page import BasePage
from selenium.webdriver.common.by import (By)

class CompletePage(BasePage):

    BUTTON_BACK_HOME = (By.ID, "back-to-products")
    COMPLETE_TEXT_ELEMENT = (By.CLASS_NAME, "complete-text")
    COMPLETE_TEXT_MESSAGE = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
    COMPLETE_HEADER_ELEMENT = (By.CLASS_NAME, "complete-header")
    COMPLETE_HEADER_MESSAGE = "Thank you for your order!"

    def checkout_finish(self):
        self.click(self.BUTTON_BACK_HOME)

    def validate_purchase_completion_message(self):
        assert self.text_of_element(self.COMPLETE_HEADER_ELEMENT) == self.COMPLETE_HEADER_MESSAGE
        assert self.text_of_element(self.COMPLETE_TEXT_ELEMENT) == self.COMPLETE_TEXT_MESSAGE