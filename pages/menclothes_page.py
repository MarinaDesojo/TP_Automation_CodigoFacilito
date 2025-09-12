from .base_page import BasePage
from selenium.webdriver.common.by import (By)
from utils.config import URLS
from utils.config import LOADING_OVERLAY
import pytest
import os

class MenClothesPage(BasePage):
    # Main
    HEADING_CATEGORY_TITLE = (By.ID, "category-title")
    TEXT_CATEGORY_DESCRIPTION = (By.ID, "category-description")

    def load(self):
        self.driver.get(URLS["men_clothes"])

    def go_to_cart_page(self):
        self.wait_until_invisible(LOADING_OVERLAY)
        self.click(self.LINK_CART)

    def go_to_product_page_by_number_1_10(self, product_number: str):
        self.wait_until_invisible(LOADING_OVERLAY)
        if not product_number.isdigit() or not (1 <= int(product_number) <= 10):
            raise ValueError("product_number has to be between '1' and '10'")
        product_detail_link = (By.CSS_SELECTOR, f'[href="/product/{product_number}"]')
        self.click(product_detail_link)

    def add_product_to_cart_by_number_1_10(self, product_number: str):
        self.wait_until_invisible(LOADING_OVERLAY)
        if not product_number.isdigit() or not (1 <= int(product_number) <= 10):
            raise ValueError("product_number has to be between '1' and '10'")
        add_button = (By.ID, f"add-to-cart-{product_number}")
        self.click(add_button)

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