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
from pages.menclothes_page import MenClothesPage
from pages.product_detail_page import ProductPage
from pages.specialdeals_page import SpecialDealsPage
from pages.womenclothes_page import WomenClothesPage
from tests.conftest import driver
from utils.config import EMAIL_USER, PASSWORD, FIRST_NAME, LAST_NAME, ZIP_CODE, PHONE_NUMBER, ADDRESS, CITY, COUNTRY

@pytest.mark.search
def test_header_search(driver):
    header = HeaderPage(driver)

    header.load()
    header.search_product("smartphone")

@pytest.mark.navigation
def test_categories_button_and_submenu_hover(driver):
    header = HeaderPage(driver)

    header.load()
    header.open_categories_menu_hover()
    header.visibility_option_categories_menu()
    header.go_to_men_clothes_categories_menu()
# Fail

@pytest.mark.navigation
def test_categories_button_and_submenu_click(driver):
    header = HeaderPage(driver)

    header.load()
    header.open_categories_menu_click()
    header.visibility_option_categories_menu()
    header.go_to_men_clothes_categories_menu()
# Fail

@pytest.mark.navigation
def test_categories_button_and_submenu_with_keyboard_1(driver):
    header = HeaderPage(driver)

    header.load()
    header.navigate_to_categories_menu_keyboard("men_clothes", 1)

def test_categories_button_and_submenu_with_keyboard_2(driver):
    header = HeaderPage(driver)

    header.load()
    header.navigate_to_categories_menu_keyboard("women_clothes", 2)

def test_categories_button_and_submenu_with_keyboard_3(driver):
    header = HeaderPage(driver)

    header.load()
    header.navigate_to_categories_menu_keyboard("electronics", 3)

def test_categories_button_and_submenu_with_keyboard_4(driver):
    header = HeaderPage(driver)

    header.load()
    header.navigate_to_categories_menu_keyboard("books", 4)

def test_categories_button_and_submenu_with_keyboard_5(driver):
    header = HeaderPage(driver)

    header.load()
    header.navigate_to_categories_menu_keyboard("groceries", 5)

def test_categories_button_and_submenu_with_keyboard_6(driver):
    header = HeaderPage(driver)

    header.load()
    header.navigate_to_categories_menu_keyboard("special_deals", 6)


@pytest.mark.content_verification
def test_product_detail_pages_work(driver):
    pdp = ProductPage(driver)

    pdp.assert_all_product_titles_present()
    time.sleep(2)


@pytest.mark.content_verification
def test_plp_order_books_page(driver):
    books = BooksPage(driver)

    books.load()
    books.test_product_card_action_elements_order_in_dom()
    books.test_visual_order_of_product_actions()

def test_plp_order_electronics_page(driver):
    electronics = ElectronicsPage(driver)

    electronics.load()
    electronics.test_product_card_action_elements_order_in_dom()
    electronics.test_visual_order_of_product_actions()

def test_plp_order_groceries_page(driver):
    groceries = GroceriesPage(driver)

    groceries.load()
    groceries.test_product_card_action_elements_order_in_dom()
    groceries.test_visual_order_of_product_actions()

def test_plp_order_men_clothes_page(driver):
    men_clothes = MenClothesPage(driver)

    men_clothes.load()
    men_clothes.test_product_card_action_elements_order_in_dom()
    men_clothes.test_visual_order_of_product_actions()

def test_plp_order_women_clothes_page(driver):
    women_clothes = WomenClothesPage(driver)

    women_clothes.load()
    women_clothes.test_product_card_action_elements_order_in_dom()
    women_clothes.test_visual_order_of_product_actions()


@pytest.mark.content_verification
def test_empty_cart(driver):
    cart = CartPage(driver)

    cart.load()
    cart.cart_empty_verification()
    cart.verify_cart_empty_text()

def test_empty_cart_from_full(driver):
    cart = CartPage(driver)
    homepage = HomePage(driver)
    groceries = GroceriesPage(driver)
    header = HeaderPage(driver)

    homepage.load()
    homepage.go_to_groceries_page()
    groceries.add_product_to_cart_by_number_41_50("42")
    header.go_to_cart_page()
    cart.remove_from_cart("Whole Wheat Bread")
    cart.cart_empty_verification()
    cart.verify_cart_empty_text()


@pytest.mark.navigation
def test_carousel_slides_1(driver):
    homepage = HomePage(driver)

    homepage.load()
    homepage.rotate_carousel_left()
    homepage.rotate_carousel_left()
    homepage.click_visible_slide_button()
    time.sleep(2)

def test_carousel_slides_2(driver):
    homepage = HomePage(driver)

    homepage.load()
    homepage.rotate_carousel_right()
    homepage.rotate_carousel_right()
    homepage.rotate_carousel_right()
    homepage.click_visible_slide_button()
    time.sleep(2)
# Fails

def test_carousel_slides_3(driver):
    homepage = HomePage(driver)

    homepage.load()
    homepage.rotate_carousel_right()
    homepage.rotate_carousel_left()
    homepage.rotate_carousel_left()
    homepage.click_visible_slide_button()
    time.sleep(2)
# Fails


@pytest.mark.navigation
def test_general_navigation(driver):
    header = HeaderPage(driver)
    homepage = HomePage(driver)

    header.load()
    homepage.go_to_men_clothes_page()
    header.go_to_homepage()
    homepage.go_to_women_clothes_page()
    header.go_to_homepage()
    homepage.go_to_electronics_page()
    header.go_to_homepage()
    homepage.go_to_books_page()
    header.go_to_homepage()
    homepage.go_to_groceries_page()
    header.go_to_homepage()
    homepage.go_to_special_deals_page()


@pytest.mark.shop
def test_add_to_cart_buttons_books_page(driver):
    books = BooksPage(driver)

    books.load()
    books.add_products_31_to_40_to_cart()
# Fails

def test_add_to_cart_buttons_electronics_page(driver):
    electronics = ElectronicsPage(driver)

    electronics.load()
    electronics.add_products_21_to_30_to_cart()
# Fails

def test_add_to_cart_buttons_groceries_page(driver):
    groceries = GroceriesPage(driver)

    groceries.load()
    groceries.add_products_41_to_50_to_cart()
# Fails

def test_add_to_cart_buttons_men_clothes_page(driver):
    men_clothes = MenClothesPage(driver)

    men_clothes.load()
    men_clothes.add_products_1_to_10_to_cart()
# Fails

def test_add_to_cart_buttons_women_clothes_page(driver):
    women_clothes = WomenClothesPage(driver)

    women_clothes.load()
    women_clothes.add_products_11_to_20_to_cart()
# Fails


@pytest.mark.navigation
def test_books_page_view_detail_links(driver):
    books = BooksPage(driver)

    books.load()
    books.verify_all_view_details_links_by_number_31_40()

def test_electronics_page_view_detail_links(driver):
    electronics = ElectronicsPage(driver)

    electronics.load()
    electronics.verify_all_view_details_links_by_number_21_30()

def test_groceries_page_view_detail_links(driver):
    groceries = GroceriesPage(driver)

    groceries.load()
    groceries.verify_all_view_details_links_by_number_41_50()

def test_men_clothes_page_view_detail_links(driver):
    men_clothes = MenClothesPage(driver)

    men_clothes.load()
    men_clothes.verify_all_view_details_links_by_number_1_10()

def test_women_clothes_view_detail_links(driver):
    women_clothes = WomenClothesPage(driver)

    women_clothes.load()
    women_clothes.verify_all_view_details_links_by_number_11_20()
