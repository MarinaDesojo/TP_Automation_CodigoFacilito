from .base_page import BasePage
from selenium.webdriver.common.by import (By)
from utils.config import URLS
from utils.config import LOADING_OVERLAY
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import os

class WomenClothesPage(BasePage):
    # Header
    TEXT_CART_BADGE = (By.CSS_SELECTOR, 'a[href="/cart"] button > div.rounded-full.absolute')
    # Main
    HEADING_CATEGORY_TITLE = (By.ID, "category-title")
    TEXT_CATEGORY_DESCRIPTION = (By.ID, "category-description")

    def load(self):
        self.driver.get(URLS["women_clothes"])
        self.assert_url("women_clothes")
        self.wait_until_invisible(LOADING_OVERLAY)

    def go_to_product_page_by_number_11_20(self, product_number: str):
        if not product_number.isdigit() or not (11 <= int(product_number) <= 20):
            raise ValueError("product_number has to be between '11' and '20'")
        product_detail_link = (By.CSS_SELECTOR, f'[href="/product/{product_number}"]')
        self.click(product_detail_link)
        self.wait_until_invisible(LOADING_OVERLAY)

    def verify_all_view_details_links_by_number_11_20(self):
        errors = []

        for product_number in range(11, 21):
            product_id = str(product_number)

            try:
                name_locator = (By.ID, f"product-name-{product_id}")
                product_name = self.text_of_element(name_locator).strip()

                view_details_link = (By.ID, f"view-details-{product_id}")
                self.click(view_details_link)

                expected_url_suffix = f"/product/{product_id}"
                WebDriverWait(self.driver, 5).until(EC.url_contains(expected_url_suffix))
                current_url = self.driver.current_url

                if not current_url.endswith(expected_url_suffix):
                    errors.append(
                        f" Product number {product_id} ('{product_name}'): "
                        f"Wrong URL. Expected: '{expected_url_suffix}', Current: '{current_url}'"
                    )

            except Exception as e:
                name = locals().get("product_name", "Unknown")
                errors.append(f"Product number {product_id} ('{name}'): {e}")

            finally:
                self.driver.get(URLS["women_clothes"])
                self.assert_url("women_clothes")
                self.wait_until_invisible(LOADING_OVERLAY)

        if errors:
            raise AssertionError(
                "\nErrors were found when verifying 'View Details' links:\n" + "\n".join(errors)
            )

    def add_product_to_cart_by_number_11_20(self, product_number: str):
        if not product_number.isdigit() or not (11 <= int(product_number) <= 20):
            raise ValueError("product_number has to be between '11' and '20'")
        add_button = (By.ID, f"add-to-cart-{product_number}")
        self.click(add_button)

    def add_products_11_to_20_to_cart(self):
        errors = []
        cart_expected = 0

        for product_number in range(11, 21):
            cart_expected += 1
            try:
                product_id_str = str(product_number)
                name_locator = (By.ID, f"product-name-{product_id_str}")
                product_name = self.text_of_element(name_locator).strip()

                self.add_product_to_cart_by_number_11_20(product_id_str)

                current_badge = int(self.text_of_element(self.TEXT_CART_BADGE))
                if current_badge != cart_expected:
                    errors.append(
                        f"Product {product_number} ('{product_name}'): "
                        f"Expected cart badge to show {cart_expected}, but got {current_badge}"
                    )
                    cart_expected = current_badge

            except Exception as e:
                name = product_name if 'product_name' in locals() else 'Unknown'
                errors.append(f"Product {product_number} ('{name}'): {e}")

        if errors:
            raise AssertionError(
                f"\nErrors were found while adding products to the cart:\n" + "\n".join(errors)
            )

    def get_product_action_elements_container(self):
        return self.driver.find_elements(By.CLASS_NAME, "product-actions")

    def test_product_card_action_elements_order_in_dom(product_list_page):
        cards = product_list_page.get_product_action_elements_container()
        assert cards, "Product cards were not found"

        for index, card in enumerate(cards):
            children = card.find_elements(By.XPATH, "./*")
            assert len(children) >= 2, f"Card #{index} has not enough children"
            # Buscar los índices de cada elemento
            link_index = next((i for i, el in enumerate(children) if "flex-1" in el.get_attribute("class").split()), -1)
            button_index = next((i for i, el in enumerate(children) if "add-to-cart-btn" in el.get_attribute("class").split()), -1)
            # Asegurar que ambos elementos existan
            assert link_index != -1, f"Product link not found on product card #{index}"
            assert button_index != -1, f"Add to cart button not found on product card #{index}"
            # Verificar el orden
            assert link_index < button_index, f"On the card #{index}, the button is before the link in the DOM"

    def test_visual_order_of_product_actions(product_list_page):
        action_containers = product_list_page.get_product_action_elements_container()
        assert action_containers, "Product action containers were not found (.product-actions)."

        errors = []
        os.makedirs("screenshots", exist_ok=True)

        for index, actions_container in enumerate(action_containers):
            try:
                product_id = actions_container.get_attribute("id").split("-")[-1]
            except Exception:
                product_id = f"desconocido_{index}"
            # Buscar el contenedor padre con id 'product-content-{id}'
            try:
                parent_container = actions_container.find_element(By.XPATH,
                                                                  f"../..")  # dos niveles arriba para llegar a product-content-31
                product_name_el = parent_container.find_element(By.CLASS_NAME, "product-name")
                product_name = product_name_el.text.strip()
            except Exception:
                product_name = f"Unknown product #{product_id}"

            try:
                link_wrapper = actions_container.find_element(By.CLASS_NAME, "flex-1")
                add_to_cart_btn = actions_container.find_element(By.CLASS_NAME, "add-to-cart-btn")
            except Exception as e:
                errors.append(f"{product_name} (ID {product_id}): Missing elements: {e}")
                actions_container.screenshot(f"screenshots/missing_elements_{product_id}.png")
                continue

            link_x = link_wrapper.location['x']
            button_x = add_to_cart_btn.location['x']

            if link_x >= button_x:
                errors.append(
                    f"{product_name} (ID {product_id}): 'View Details' link is not the left of 'Add to Cart' button")
                actions_container.screenshot(f"screenshots/wrong_order_{product_id}.png")

        if errors:
            all_errors = "\n".join(errors)
            pytest.fail(f"Product action elements were found in the wrong order:\n{all_errors}")