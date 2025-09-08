from .base_page import BasePage
from selenium.webdriver.common.by import (By)



class HomePage(BasePage):
    # URL
    URL = "https://shophub-commerce.vercel.app/"  # mejor practica en un archivo de datos modularizado
    # Header
    LINK_HOMEPAGE = (By.CSS_SELECTOR, "a.mr-6.flex.items-center.space-x-2")
    BUTTON_CATEGORIES = (By.XPATH, '//button[contains(., "Categories")]')
    INPUT_SEARCH = (By.XPATH, '//input[@placeholder="Search products..."]')
    LINK_LOGIN = (By.XPATH, '//a[@href="/login"]')
    LINK_SIGNUP = (By.XPATH, '//a[@href="/signup"]')
    LINK_CART = (By.XPATH, '//a[@href="/cart"]')
    TEXT_CART_BADGE = (By.CSS_SELECTOR, 'a[href="/cart"] button > div.rounded-full.absolute')
    SUBMENU_CATEGORIES = (By.XPATH, '//div[@data-orientation="horizontal"]//div[contains(@class, "grid")]')
    LINK_SUBMENU_CATEGORIES = (By.XPATH, '//a[href="/categories/men-clothes" and @data-radix-collection-item]')
    # Overlay
    LOADING_OVERLAY = (By.CSS_SELECTOR, 'div.fixed.inset-0.z-50.flex.items-center.justify-center.bg-background\\/70')
    # Main
    # Main - Carousel controls
    BUTTON_CAROUSEL_LEFT = (By.CSS_SELECTOR, 'button svg.lucide-chevron-left')
    BUTTON_CAROUSEL_RIGHT = (By.CSS_SELECTOR, 'button svg.lucide-chevron-right')
    BUTTON_DOT_ONE = (By.XPATH, "/html/body/main/div/section[1]/div[2]/button[1]")
    BUTTON_DOT_TWO = (By.XPATH, "/html/body/main/div/section[1]/div[2]/button[2]")
    BUTTON_DOT_THREE = (By.XPATH, "/html/body/main/div/section[1]/div[2]/button[3]")
    # Main - Carousel slides
    HEADING_FRESH_GROCERIES = (By.XPATH, '//h1[normalize-space()="Fresh Groceries"]')
    LINK_ORDER_NOW_GROCERIES = (By.XPATH, '//button[text()="Order Now"]/ancestor::a')
    HEADING_LATEST_ELECTRONICS = (By.XPATH, '//h1[normalize-space()="Latest Electronics"]')
    LINK_EXPLORE_ELECTRONICS = (By.XPATH, '//button[text()="Explore"]/ancestor::a')
    HEADING_SUMMER_FASHION_SALE = (By.XPATH, '//h1[normalize-space()="Summer Fashion Sale"]')
    LINK_SHOP_NOW_SPECIAL_DEALS = (By.XPATH, '//button[text()="Shop Now"]/ancestor::a')
    # Main - Shop by category
    HEADING_SHOP_BY_CATEGORY = (By.XPATH, '//h2[normalize-space()="Shop by Category"]')
    LINK_CATEGORY_MEN_CLOTHES = (By.XPATH, "//h3[text()='Men's Clothes']/ancestor::a")
    LINK_CATEGORY_WOMEN_CLOTHES = (By.XPATH, "//h3[text()='Women's Clothes']/ancestor::a")
    LINK_CATEGORY_ELECTRONICS = (By.XPATH, '//h3[text()="Electronics"]/ancestor::a')
    LINK_CATEGORY_BOOKS = (By.XPATH, '//h3[text()="Books"]/ancestor::a')
    LINK_CATEGORY_GROCERIES = (By.XPATH, '//h3[text()="Groceries"]/ancestor::a')
    # Main - Special deals
    HEADING_SPECIAL_DEALS = (By.XPATH, '//h2[normalize-space()="Special Deals"]')
    LINK_VIEW_ALL_DEALS = (By.XPATH, '//button[text()="View All Deals"]/ancestor::a')

    def load(self):
        self.visit(self.URL)

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

    def go_to_homepage(self):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        self.click(self.LINK_HOMEPAGE)

    def go_to_special_deals_page(self):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        self.click(self.LINK_VIEW_ALL_DEALS)

    def rotate_carousel_left(self):
        #self.wait_until_invisible(self.LOADING_OVERLAY)
        svg_icon = self.driver.find_element(*self.BUTTON_CAROUSEL_LEFT)
        button = svg_icon.find_element(By.XPATH, './ancestor::button')
        button.click()

    # def rotate_carousel_right(self):
    #     self.wait_until_invisible(self.LOADING_OVERLAY)
    #     svg_icon = self.driver.find_element(*self.BUTTON_CAROUSEL_RIGHT)
    #     button = svg_icon.find_element(By.XPATH, './ancestor::button')
    #     button.click()

    def rotate_carousel_right(self):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        self.click(self.BUTTON_CAROUSEL_RIGHT)

    def go_to_groceries_page_carousel(self):
        self.wait_until_invisible(self.LOADING_OVERLAY)
        self.wait_until_visible(self.LINK_ORDER_NOW_GROCERIES)
        self.click(self.LINK_ORDER_NOW_GROCERIES)

    def check_cart_badge_amount(self, amount: int):
        badge = self.text_of_element(self.TEXT_CART_BADGE)
        if not (int(badge) == amount):
            raise ValueError("amount debe ser igual a la cantidad de productos agregados al carro")
        print(badge)