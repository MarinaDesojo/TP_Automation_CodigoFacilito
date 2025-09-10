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

    def load(self):
        self.driver.get(URLS["login"])

    def fill_login_form(self, email: str, password: str):
        self.wait_until_invisible(LOADING_OVERLAY)
        self.type(self.INPUT_EMAIL, email)
        self.type(self.INPUT_PASSWORD, password)
        self.click(self.BUTTON_LOGIN)



