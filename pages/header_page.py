from .base_page import BasePage
from selenium.webdriver.common.by import (By)
from utils.config import URLS
from utils.config import LOADING_OVERLAY

class HeaderPage(BasePage):
    # Header
    LINK_HOMEPAGE = (By.CSS_SELECTOR, "a.mr-6.flex.items-center.space-x-2")
    BUTTON_CATEGORIES = (By.XPATH, '//button[contains(., "Categories")]')
    INPUT_SEARCH = (By.XPATH, '//input[@placeholder="Search products..."]')
    LINK_LOGIN = (By.XPATH, '//a[@href="/login"]')
    LINK_SIGNUP = (By.XPATH, '//a[@href="/signup"]')
    LINK_CART = (By.XPATH, '//a[@href="/cart"]')
    TEXT_CART_BADGE = (By.CSS_SELECTOR, 'a[href="/cart"] button > div.rounded-full.absolute')
    SUBMENU_CATEGORIES = (By.XPATH, '//div[@data-orientation="horizontal"]//div[contains(@class, "grid")]')
    LINK_SUBMENU_CATEGORIES_MEN_CLOTHES = (By.XPATH, '//a[href="/categories/men-clothes" and @data-radix-collection-item]')

    def load(self):
        self.driver.get(URLS["homepage"])
        self.assert_url("homepage")

    def go_to_homepage(self):
        self.click(self.LINK_HOMEPAGE)
        self.assert_url("homepage")
        self.wait_until_invisible(LOADING_OVERLAY)

    def open_categories_menu_hover(self):
        self.hover(self.BUTTON_CATEGORIES)

    def open_categories_menu_click(self):
        self.click(self.BUTTON_CATEGORIES)

    def visibility_option_categories_menu(self, is_visible=None):
        self.element_is_visible(self.SUBMENU_CATEGORIES)
        print(f"SUBMENU_CATEGORIES visible? {bool(is_visible)}")

    def go_to_men_clothes_categories_menu(self):
        self.click(self.LINK_SUBMENU_CATEGORIES_MEN_CLOTHES)

    def navigate_to_categories_menu_keyboard(self, path, arrow_presses: int = 1):
        self.keyboard_navigation_tab(2)
        self.keyboard_access_element()
        for _ in range(int(arrow_presses)):
            self.keyboard_navigation_arrow_down()
        self.keyboard_access_element()
        self.assert_url(path)
        self.wait_until_invisible(LOADING_OVERLAY)

    def search_product(self, search):
        self.type(self.INPUT_SEARCH, search)

    def go_to_login_page(self):
        self.click(self.LINK_LOGIN)
        self.assert_url("login")
        self.wait_until_invisible(LOADING_OVERLAY)

    def go_to_signup_page(self):
        self.click(self.LINK_SIGNUP)
        self.assert_url("signup")
        self.wait_until_invisible(LOADING_OVERLAY)

    def go_to_cart_page(self):
        self.click(self.LINK_CART)
        self.assert_url("cart")
        self.wait_until_invisible(LOADING_OVERLAY)

    def check_cart_badge_amount(self, amount: int):
        badge = int(self.text_of_element(self.TEXT_CART_BADGE))
        assert badge == amount, f"Expected cart badge to show {amount} but got {badge}"
