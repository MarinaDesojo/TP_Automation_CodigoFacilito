from .base_page import BasePage
from selenium.webdriver.common.by import (By)
from utils.config import URLS
from utils.config import LOADING_OVERLAY

class HomePage(BasePage):
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
        self.driver.get(URLS["homepage"])

    def go_to_electronics_page(self):
        self.click(self.LINK_CATEGORY_ELECTRONICS)
        self.assert_url("electronics")
        self.wait_until_invisible(LOADING_OVERLAY)

    def go_to_books_page(self):
        self.click(self.LINK_CATEGORY_BOOKS)
        self.assert_url("books")
        self.wait_until_invisible(LOADING_OVERLAY)

    def go_to_special_deals_page(self):
        self.click(self.LINK_VIEW_ALL_DEALS)
        self.assert_url("special_deals")
        self.wait_until_invisible(LOADING_OVERLAY)

    def rotate_carousel_left(self):
        svg_icon = self.driver.find_element(*self.BUTTON_CAROUSEL_LEFT)
        button = svg_icon.find_element(By.XPATH, './ancestor::button')
        button.click()

    def rotate_carousel_right(self):
        svg_icon = self.driver.find_element(*self.BUTTON_CAROUSEL_RIGHT)
        button = svg_icon.find_element(By.XPATH, './ancestor::button')
        button.click()

    def go_to_groceries_page_carousel(self):
        self.wait_until_visible(self.LINK_ORDER_NOW_GROCERIES)
        self.click(self.LINK_ORDER_NOW_GROCERIES)
        self.assert_url("groceries")
        self.wait_until_invisible(LOADING_OVERLAY)


