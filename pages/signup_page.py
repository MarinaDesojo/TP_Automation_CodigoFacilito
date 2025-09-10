from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.config import URLS
from utils.config import LOADING_OVERLAY

class SignUpPage(BasePage): #como parametro recibe basepage para poder replicar los metodos
    # Main
    HEADING_SIGNUP = (By.XPATH, '//div[normalize-space()="Sign Up"]')
    INPUT_FIRST_NAME = (By.ID, "firstName")
    INPUT_LAST_NAME = (By.ID, "lastName")
    INPUT_EMAIL = (By.ID, "email")
    INPUT_ZIP_CODE = (By.ID, "zipCode")
    INPUT_PASSWORD = (By.ID, "password")
    BUTTON_SIGNUP = (By.XPATH, '//button[@type="submit" and text()="Sign Up"]')

    def load(self):
        self.driver.get(URLS["signup"])

    def fill_sign_up_form(self, first_name: str, last_name: str, email: str, zip_code: str, password: str):
        self.type(self.INPUT_FIRST_NAME, first_name)
        self.type(self.INPUT_LAST_NAME, last_name)
        self.type(self.INPUT_EMAIL, email)
        self.type(self.INPUT_ZIP_CODE, zip_code)
        self.type(self.INPUT_PASSWORD, password)
        self.click(self.BUTTON_SIGNUP)

