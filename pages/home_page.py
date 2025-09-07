from .base_page import BasePage
from selenium.webdriver.common.by import (By)



class HomePage(BasePage):
    LINK_HOMEPAGE = (By.CLASS_NAME, "mr-6 flex items-center space-x-2")
    #BUTTON_CATEGORIES = (By.ID, "radix-«R2bb»-trigger-radix-«Rebb»")
    BUTTON_CATEGORIES = (By.XPATH, '//button[contains(., "Categories")]')
    INPUT_SEARCH = (By.XPATH, '//input') #funciona porque es el unico input tag de la homepage
    LINK_LOGIN = (By.XPATH, '//a[@href="/login"]')
    LINK_SIGNUP = (By.XPATH, '//a[@href="/signup"]')
    LINK_CART = (By.XPATH, '//a[@href="/cart"]')
    SUBMENU_CATEGORIES = (By.XPATH, '//div[@data-orientation="horizontal"]//div[contains(@class, "grid")]')
    LINK_SUBMENU_CATEGORIES = (By.XPATH, '//a[href="/categories/men-clothes" and @data-radix-collection-item]')
    LINK_CATEGORY_ELECTRONICS = (By.XPATH, '//h3[text()="Electronics"]/ancestor::a')

    LOADING_OVERLAY = (By.CSS_SELECTOR, 'div.fixed.inset-0.z-50.flex.items-center.justify-center.bg-background\\/70')

    URL = "https://shophub-commerce.vercel.app/" #mejor practica en un archivo de datos modularizado

    #Acciones/metodos
    def load(self): #se usa la palabra load para cargar la pagina
        self.visit(self.URL) #hay que indicar el SELF para que sepa que viene de la misma clase esta donde estamos

    def go_to_cart_page(self):
        self.click(self.LINK_CART)

    def go_to_login_page(self):
        self.click(self.LINK_LOGIN)

    def go_to_signup_page(self):
        self.click(self.LINK_SIGNUP)

    def search_product(self, search):
        self.type(self.INPUT_SEARCH, search)

    def open_categories_menu(self):
        self.hover(self.BUTTON_CATEGORIES)

    def visibility_option_categories_menu(self, is_visible=None):
        self.element_is_visible(self.SUBMENU_CATEGORIES)
        print(f"SUBMENU_CATEGORIES visible? {bool(is_visible)}")

    # def select_option_categories_menu(self, is_clickable=None):
    #     self.element_is_clickable(self.LINK_SUBMENU_CATEGORIES)
    #     print(f"LINK_SUBMENU_CATEGORIES clickable? {bool(is_clickable)}")
    #     #self.click(self.LINK_SUBMENU_CATEGORIES)

    # def visibility_option_categories_menu(self):
    #     try:
    #         self.element_is_visible(self.LINK_SUBMENU_CATEGORIES, timeout=5)
    #         print("✅ Link 'Men's Clothes' visible")
    #     except Exception as e:
    #         print("❌ Link 'Men's Clothes' NO visible:", e)
    #
    # def debug_check_submenu_presence(self):
    #     elements = self.driver.find_elements(*self.SUBMENU_CATEGORIES)
    #     print(f"¿Elemento SUBMENU_CATEGORIES está en el DOM? {'Sí' if elements else 'No'}")

    def go_to_electronics_page(self):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        self.click(self.LINK_CATEGORY_ELECTRONICS)
