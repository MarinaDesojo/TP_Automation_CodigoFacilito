from .base_page import BasePage
from selenium.webdriver.common.by import (By)
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import get_product_url
from utils.config import BASE_URL
from utils.config import LOADING_OVERLAY


class ProductPage(BasePage):
    # Main - armados con 24 porque no hice todas las funciones custom
    HEADING_CATEGORY_TITLE = (By.ID, "product-main-title-24")
    TEXT_CATEGORY_DESCRIPTION = (By.ID, "product-category-24")
    TEXT_PRODUCT_PRICE = (By.ID, "product-main-price-24")
    TEXT_PRODUCT_DESCRIPTION_TITLE = (By.ID, "product-desc-title-24")
    TEXT_PRODUCT_DESCRIPTION = (By.ID, "product-desc-text-24")
    TEXT_QTY = (By.ID, "quantity-display-24")
    CONTAINER_PRODUCT_FEATURES = (By.ID, "product-features-24")
    TEXT_FEATURE_SHIPPING = (By.ID, "feature-shipping-24")
    TEXT_FEATURE_RETURN = (By.ID, "feature-returns-24")
    TEXT_FEATURE_PAYMENT = (By.ID, "feature-payment-24")

    def load(self, product_number):
        url = get_product_url(product_number)
        self.driver.get(url)

    def increase_product_qty(self, product_number: str):
        if not product_number.isdigit() or not (1 <= int(product_number) <= 50):
            raise ValueError("product_number has to be between '1' and '50'")
        increase = (By.ID, f"quantity-increase-{product_number}")
        self.click(increase)

    def decrease_product_qty(self, product_number: str):
        if not product_number.isdigit() or not (1 <= int(product_number) <= 50):
            raise ValueError("product_number has to be between '1' and '50'")
        decrease = (By.ID, f"quantity-decrease-{product_number}")
        self.click(decrease)

    def add_to_cart(self, product_number: str):
        if not product_number.isdigit() or not (1 <= int(product_number) <= 50):
            raise ValueError("product_number has to be between '1' and '50'")
        add_to_cart = (By.ID, f"add-to-cart-main-{product_number}")
        self.click(add_to_cart)

    def go_back_to_category(self, product_number: str):
        self.wait_until_invisible(LOADING_OVERLAY)
        if not product_number.isdigit() or not (1 <= int(product_number) <= 50):
            raise ValueError("product_number has to be between '1' and '50'")
        back = (By.ID, f"back-btn-{product_number}")
        self.click(back)
        self.wait_until_invisible(LOADING_OVERLAY)

    def mark_as_favorite(self, product_number: str):
        self.wait_until_invisible(LOADING_OVERLAY)
        if not product_number.isdigit() or not (1 <= int(product_number) <= 50):
            raise ValueError("product_number has to be between '1' and '50'")
        fav = (By.ID, f"wishlist-{product_number}")
        self.click(fav)

    def assert_all_product_titles_present(self, start=1, end=50):
        errors = []

        for product_number in range(start, end + 1):
            product_url = f"{BASE_URL}product/{product_number}"
            self.driver.get(product_url)

            try:
                h1_locator = (By.ID, f"product-main-title-{product_number}")
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(h1_locator))
            except Exception:
                errors.append(f"Missing: {product_url} does not contain an h1 related to the product name.'>")

        if errors:
            error_report = "\n".join(errors)
            raise AssertionError(f"\nErrors (404 Product Not Found) were found in {len(errors)} products:\n{error_report}")
        else:
            print(f"All product titles from {start} to {end} were verified correctly.")
