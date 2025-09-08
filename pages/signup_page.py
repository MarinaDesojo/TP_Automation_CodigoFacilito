from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage): #como parametro recibe basepage para poder replicar los metodos
    # URL
    URL = "https://shophub-commerce.vercel.app/signup"  # mejor practica en un archivo de datos modularizado
    # Header
    LINK_HOMEPAGE = (By.CSS_SELECTOR, "a.mr-6.flex.items-center.space-x-2")
    BUTTON_CATEGORIES = (By.XPATH, '//button[contains(., "Categories")]')
    INPUT_SEARCH = (By.XPATH, '//input[@placeholder="Search products..."]')
    LINK_LOGIN = (By.XPATH, '//a[@href="/login"]')
    LINK_SIGNUP = (By.XPATH, '//a[@href="/signup"]')
    LINK_CART = (By.XPATH, '//a[@href="/cart"]')
    SUBMENU_CATEGORIES = (By.XPATH, '//div[@data-orientation="horizontal"]//div[contains(@class, "grid")]')
    LINK_SUBMENU_CATEGORIES = (By.XPATH, '//a[href="/categories/men-clothes" and @data-radix-collection-item]')
    # Overlay
    LOADING_OVERLAY = (By.CSS_SELECTOR, 'div.fixed.inset-0.z-50.flex.items-center.justify-center.bg-background\\/70')
    # Main
    HEADING_SIGNUP = (By.XPATH, '//div[normalize-space()="Sign Up"]')
    INPUT_FIRST_NAME = (By.ID, "firstName")
    INPUT_LAST_NAME = (By.ID, "lastName")
    INPUT_EMAIL = (By.ID, "email")
    INPUT_ZIP_CODE = (By.ID, "zipCode")
    INPUT_PASSWORD = (By.ID, "password")
    BUTTON_SIGNUP = (By.XPATH, '//button[@type="submit" and text()="Sign Up"]')

    def load(self):
        self.visit(self.URL)

    def fill_sign_up_form(self, first_name: str, last_name: str, email: str, zip_code: str, password: str):
        self.type(self.INPUT_FIRST_NAME, first_name)
        self.type(self.INPUT_LAST_NAME, last_name)
        self.type(self.INPUT_EMAIL, email)
        self.type(self.INPUT_ZIP_CODE, zip_code)
        self.type(self.INPUT_PASSWORD, password)
        self.click(self.BUTTON_SIGNUP)

