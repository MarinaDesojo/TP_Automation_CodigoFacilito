from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage): #como parametro recibe basepage para poder replicar los metodos
    #Datos de prueba
    URL = "https://shophub-commerce.vercel.app/login" #mejor practica en un archivo de datos modularizado

    #Selectores
    INPUT_EMAIL = (By.ID, "email")
    INPUT_PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.XPATH, '//button[@type="submit" and text()="Login"]') #convencion de hector, primero elemento despues nombre

    #Acciones/metodos
    def load(self): #se usa la palabra load para cargar la pagina
        self.visit(self.URL) #hay que indicar el SELF para que sepa que viene de la misma clase esta donde estamos

    def login_as_user(self, email: str, password: str):
        self.type(self.INPUT_EMAIL, email)
        self.type(self.INPUT_PASSWORD, password)
        self.click(self.BUTTON_LOGIN)

    #def assert_inventory_url(self): #en realidad tiene que ir a la web de productos
    #    assert "inventory" in driver.current_url, "No te encuentras en URL /inventory" #valida que la palabra inventory esta en la URL

