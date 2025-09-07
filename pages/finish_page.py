from .base_page import BasePage
from selenium.webdriver.common.by import (By)

class FinishPage(BasePage):
    BUTTON_FINISH = (By.ID, "finish")
    CHECK_INFO = (By.CLASS_NAME, "summary_info_label")
    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")

    def finish_checkout(self):
        self.click(self.BUTTON_FINISH)

    def check_info(self):
    #    self.text = self.driver.find_elements(By.CLASS_NAME, "summary_info_label")
        self.text_of_element(self.CHECK_INFO)

    def total_price(self):
        self.element_is_visible(self.TOTAL_PRICE)
