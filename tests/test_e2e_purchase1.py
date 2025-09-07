import time

import pytest
#page objects
from pages.base_page import BasePage #importa la clase base page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.products_page import ProductPage
from pages.finish_page import FinishPage
from pages.complete_page import CompletePage
from pages.home_page import HomePage
from pages.electronics_page import ElectronicsPage
from pages.product_detail_page import PDPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage
from tests.conftest import driver

#no deberian estar aca, temporal
EMAIL_USER = "user@user.com"
PASSWORD = "password1234"
EMAIL_USER_WRONG = "notanemail"
FIRST_NAME = "Carlos"
LAST_NAME = "Perez"
ZIP_CODE = "123456"
PHONE_NUMBER = "0123456789"
ADDRESS = "123 Main St."
CITY = "fakecity"
COUNTRY = "fakecountry"

@pytest.mark.e2e #e2e = end to end, de inicio a fin
def test_user_purchase_product_positive(driver):
    products = ProductPage(driver) #estas se llaman instancias
    login = LoginPage(driver)
    cart = CartPage(driver)
    finish = FinishPage(driver)
    complete = CompletePage(driver)
    homepage = HomePage(driver)

    login.load()
    login.login_as_user(EMAIL_USER, PASSWORD)
    products.add_product_by_name("sauce-labs-backpack")
    products.go_to_shopping_cart()
    cart.go_to_checkout()
    cart.complete_information_form(FIRST_NAME, LAST_NAME, POSTAL_CODE)
    finish.check_info()
    finish.total_price()
    finish.finish_checkout()
    complete.validate_purchase_completion_message()
    complete.checkout_finish()


    #Ir a la URL del login
    #Login -> llenar los campos


def test_homepage_to_login_page_login(driver):
    homepage = HomePage(driver)
    login = LoginPage(driver)

    homepage.load()
    homepage.go_to_login_page()
    login.login_as_user(EMAIL_USER, PASSWORD)

def test_homepage_to_login_page_login_fail(driver): #no se por que no falla.. cuando lo hago a mano si falla
    homepage = HomePage(driver)
    login = LoginPage(driver)

    homepage.load()
    homepage.go_to_login_page()
    login.login_as_user(EMAIL_USER_WRONG, PASSWORD)


def test_homepage_search(driver):
    homepage = HomePage(driver)

    homepage.load()
    homepage.search_product("smartphone") #la web no tiene motor de busqueda pero al menos se puede escribir en el campo


def test_homepage_categories(driver):
    homepage = HomePage(driver)

    homepage.load()
    homepage.open_categories_menu()
    #homepage.debug_check_submenu_presence()
    homepage.visibility_option_categories_menu() #esto no funciona no se por que, no ve el
    #homepage.select_option_categories_menu()


def test_shop_e2e(driver):
    homepage = HomePage(driver)
    electronics = ElectronicsPage(driver)
    pdp = PDPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    confirmation = ConfirmationPage(driver)

    homepage.load()
    homepage.go_to_electronics_page()
    electronics.go_to_product_page()
    pdp.add_product_qty()
    pdp.add_product_to_cart()
    pdp.go_to_cart_page()
    cart.go_to_checkout()
    checkout.fill_checkout_form(FIRST_NAME, LAST_NAME, EMAIL_USER, PHONE_NUMBER, ADDRESS, CITY, ZIP_CODE, COUNTRY)
    time.sleep(1)
    confirmation.return_to_home()
