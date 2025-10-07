import pytest
#page objects
from UI_project.pages.login_page import LoginPage
from UI_project.pages.signup_page import SignUpPage
from UI_project.pages.cart_page import CartPage
from UI_project.pages.checkout_page import CheckoutPage
from UI_project.pages.confirmation_page import ConfirmationPage
from UI_project.pages.electronics_page import ElectronicsPage
from UI_project.pages.header_page import HeaderPage
from UI_project.pages.home_page import HomePage
from UI_project.pages.menclothes_page import MenClothesPage
from UI_project.pages.product_detail_page import ProductPage
from conftest import driver
from UI_project.utils.config import EMAIL_USER, PASSWORD, FIRST_NAME, LAST_NAME, ZIP_CODE, PHONE_NUMBER, ADDRESS, CITY, COUNTRY


@pytest.mark.web
@pytest.mark.e2e
@pytest.mark.happy_path
@pytest.mark.shop
def test_shop_e2e(driver):
    signup = SignUpPage(driver)
    login = LoginPage(driver)
    homepage = HomePage(driver)
    electronics = ElectronicsPage(driver)
    pdp = ProductPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    confirmation = ConfirmationPage(driver)
    header = HeaderPage(driver)
    men_clothes = MenClothesPage(driver)

    homepage.load()
    header.go_to_signup_page()
    signup.fill_sign_up_form_success(FIRST_NAME, LAST_NAME, EMAIL_USER, ZIP_CODE, PASSWORD)
    signup.verify_signed_up_text()
    signup.go_to_home()

    header.go_to_login_page()
    login.fill_login_form_success(EMAIL_USER, PASSWORD)
    login.verify_logged_in_text()
    login.go_to_home()

    homepage.go_to_electronics_page()
    electronics.go_to_product_page_by_number_21_30("24")
    pdp.increase_product_qty("24")
    pdp.add_to_cart("24")
    header.check_cart_badge_amount(2)
    pdp.go_back_to_category("24")
    electronics.add_product_to_cart_by_number_21_30("22")
    header.go_to_cart_page()

    cart.increase_qty("Laptop")
    cart.decrease_qty("Smart Watch")
    cart.remove_from_cart("Laptop")
    cart.continue_shopping()

    homepage.go_to_men_clothes_page()
    men_clothes.add_product_to_cart_by_number_1_10("3")
    header.go_to_cart_page()

    cart.go_to_checkout()
    checkout.fill_checkout_form(FIRST_NAME, LAST_NAME, EMAIL_USER, PHONE_NUMBER, ADDRESS, CITY, ZIP_CODE, COUNTRY)
    confirmation.validate_purchase_completion_heading()
    confirmation.validate_purchase_completion_message()
    confirmation.return_to_home()