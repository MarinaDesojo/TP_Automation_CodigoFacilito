from .base_page import BasePage
from selenium.webdriver.common.by import (By)
from UI_project.utils.config import URLS
from UI_project.utils.config import LOADING_OVERLAY

class ConfirmationPage(BasePage):
    # Locators
    HEADING_NO_ORDER = (By.CSS_SELECTOR, ".mb-4")
    TEXT_INFORMATION = (By.CSS_SELECTOR, ".mb-8")
    LINK_RETURN_HOME= (By.XPATH, '//button[text()="Return to Home"]/ancestor::a')
    # Content
    HEADING = "No Order Found"
    TEXT_MESSAGE = "We couldn't find your order information."
    LINK_TEXT = "Return to Home"

    def load(self):
        self.driver.get(URLS["confirmation"])
        self.assert_url("confirmation")
        self.wait_until_invisible(LOADING_OVERLAY)

    def return_to_home(self):
        self.click(self.LINK_RETURN_HOME)
        self.assert_url("homepage")
        self.wait_until_invisible(LOADING_OVERLAY)

    def validate_purchase_completion_heading(self, HEADING=HEADING):
        expected_message = HEADING
        actual_message = self.text_of_element(self.HEADING_NO_ORDER)
        assert expected_message == actual_message, f"Expected: {expected_message}, Actual: {actual_message}"

    def validate_purchase_completion_message(self, TEXT_MESSAGE=TEXT_MESSAGE):
        expected_message = TEXT_MESSAGE
        actual_message = self.text_of_element(self.TEXT_INFORMATION)
        assert expected_message == actual_message, f"Expected: {expected_message}, Actual: {actual_message}"