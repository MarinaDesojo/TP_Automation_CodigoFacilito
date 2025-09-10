import time
import pytest
#page objects
from pages.books_page import BooksPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage
from pages.electronics_page import ElectronicsPage
from pages.groceries_page import GroceriesPage
from pages.header_page import HeaderPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.menclothes_page import MenClothesPage
from pages.product_detail_page import ProductPage
from pages.signup_page import SignUpPage
from pages.specialdeals_page import SpecialDealsPage
from pages.womenclothes_page import WomenClothesPage

from tests.conftest import driver

from utils.config import EMAIL_USER, PASSWORD, EMAIL_USER_WRONG, FIRST_NAME, LAST_NAME, ZIP_CODE, PHONE_NUMBER, ADDRESS, CITY, COUNTRY


@pytest.mark.login
@pytest.mark.happypath
def test_homepage_to_login_page_login(driver):
    homepage = HomePage(driver)
    login = LoginPage(driver)

    homepage.load()
    homepage.go_to_login_page()
    login.fill_login_form(EMAIL_USER, PASSWORD)
    print(EMAIL_USER,PASSWORD)

def test_homepage_to_login_page_login_fail(driver): #no se por que no falla.. cuando lo hago a mano si falla
    homepage = HomePage(driver)
    login = LoginPage(driver)

    homepage.load()
    homepage.go_to_login_page()
    login.fill_login_form(EMAIL_USER_WRONG, PASSWORD)


def test_homepage_search(driver):
    homepage = HomePage(driver)

    homepage.load()
    homepage.search_product("smartphone") #la web no tiene motor de busqueda pero al menos se puede escribir en el campo
    time.sleep(1)


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
    pdp = ProductPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    confirmation = ConfirmationPage(driver)
    header = HeaderPage(driver)

    homepage.load()
    homepage.go_to_electronics_page()
    electronics.go_to_product_page_by_number_21_30("24")
    pdp.increase_product_qty("24")
    pdp.add_to_cart("24")
    header.check_cart_badge_amount(2)
    header.go_to_cart_page()
    cart.go_to_checkout()
    checkout.fill_checkout_form(FIRST_NAME, LAST_NAME, EMAIL_USER, PHONE_NUMBER, ADDRESS, CITY, ZIP_CODE, COUNTRY)
    confirmation.return_to_home()

def test_cart(driver):
    homepage = HomePage(driver)
    cart = CartPage(driver)
    electronics = ElectronicsPage(driver)
    header = HeaderPage(driver)

    homepage.load()
    header.go_to_homepage()
    homepage.go_to_electronics_page()
    electronics.add_product_to_cart_by_number_21_30("21")
    electronics.add_product_to_cart_by_number_21_30("22") #fallan los botones de la cart page
    electronics.add_product_to_cart_by_number_21_30("30") #falla porque no existe el producto número 31
    header.go_to_cart_page()
    cart.increase_qty()
    cart.increase_qty()
    cart.decrease_qty()
    cart.remove_from_cart()
    cart.continue_shopping()


def test_homepage(driver): #hacer estas pruebas y las del locator y mostrar que fallan
    homepage = HomePage(driver)

    homepage.load()
    homepage.navigate_to_categories_menu(0,40)
    time.sleep(5)


def test_homepage1(driver): # WOOOOOO ESTE SI FUNCIONA XD LPM
    homepage = HomePage(driver)

    homepage.load()
    homepage.navigate_to_categories_menu_keyboard()
    time.sleep(5)

def test_product_page(driver):
    pdp = ProductPage(driver)

    pdp.load("30")
    time.sleep(2)

def test_cart_page_from_header_page(driver):
    header = HeaderPage(driver)
    cart = CartPage(driver)

    header.load()
    header.go_to_cart_page()
    cart.continue_shopping()
    time.sleep(2)

