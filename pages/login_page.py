from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.config import URLS
from utils.config import LOADING_OVERLAY

class LoginPage(BasePage): #como parametro recibe basepage para poder replicar los metodos
    # Main
    HEADING_LOGIN = (By.XPATH, '//div[normalize-space()="Login"]')
    INPUT_EMAIL = (By.ID, "email")
    INPUT_PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.XPATH, '//button[@type="submit" and text()="Login"]')
    # Logged in success
    HEADING_LOGGED_IN = (By.TAG_NAME, 'h1')
    HEADING_LOGGED_IN_TEXT = "Logged In"
    LINK_HOMEPAGE = (By.XPATH, '//button[text()="Go to Home"]/ancestor::a')

    def load(self):
        self.driver.get(URLS["login"])
        self.assert_url("login")

    def fill_login_form_success(self, email: str, password: str):
        self.wait_until_invisible(LOADING_OVERLAY)
        self.type(self.INPUT_EMAIL, email)
        self.type(self.INPUT_PASSWORD, password)
        self.click(self.BUTTON_LOGIN)
        self.assert_url("logged_in")
        self.wait_until_invisible(LOADING_OVERLAY)

    def fill_login_form_fail(self, email: str, password: str):
        self.type(self.INPUT_EMAIL, email)
        self.type(self.INPUT_PASSWORD, password)
        self.click(self.BUTTON_LOGIN)
        self.assert_url_negative("logged_in")

    def empty_login_form(self):
        self.click(self.BUTTON_LOGIN)
        self.assert_url_negative("logged_in")

    def verify_logged_in_text(self):
        self.assert_text_of_element(locator=self.HEADING_LOGGED_IN, expected_text=self.HEADING_LOGGED_IN_TEXT)

    def go_to_home(self):
        self.click(self.LINK_HOMEPAGE)
        self.assert_url("homepage")
        self.wait_until_invisible(LOADING_OVERLAY)
