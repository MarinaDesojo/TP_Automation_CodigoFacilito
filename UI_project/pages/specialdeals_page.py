from .base_page import BasePage
from selenium.webdriver.common.by import (By)
from UI_project.utils.config import URLS
from UI_project.utils.config import LOADING_OVERLAY


class SpecialDealsPage(BasePage):
    # Main
    HEADING_CATEGORY_TITLE = (By.ID, "category-title")
    TEXT_CATEGORY_DESCRIPTION = (By.ID, "category-description")

    def load(self):
        self.driver.get(URLS["special_deals"])
        self.assert_url("special_deals")
        self.wait_until_invisible(LOADING_OVERLAY)


