import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.config import URLS
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver) -> None:
        self.driver = driver

    def visit(self, url: str) -> None:
        self.driver.get(url)

    def click(self, locator: tuple[By, str], timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except TimeoutException:
            raise AssertionError(f"The element {locator} was not found to be clickable after {timeout} seconds.")

    def type(self, locator: tuple[By, str], text: str):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def text_of_element(self, locator: tuple[By, str]) -> str:
        return self.driver.find_element(*locator).text

    def assert_text_of_element(self, locator, expected_text: str):
        element = self.driver.find_element(*locator)
        current_text = element.text.strip()
        assert current_text == expected_text, f"Expected '{expected_text}', but got '{current_text}'"

    def element_is_visible(self, locator: tuple[By, str]) -> bool:
        return self.driver.find_element(*locator).is_displayed()

    def hover(self, locator: tuple[By, str]):
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def wait_until_invisible(self, locator, appear_timeout=0.5, disappear_timeout=10):  # espera a que aparezca y desaparezca el overlay
        try:
            WebDriverWait(self.driver, appear_timeout, poll_frequency=0.1).until(
                EC.presence_of_element_located(locator)
            )
            WebDriverWait(self.driver, disappear_timeout, poll_frequency=0.1).until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            pass

    def wait_until_visible(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout, poll_frequency=0.1).until(
                EC.visibility_of_element_located(locator)
            )

            # Make sure it's on viewport
            is_in_viewport = self.driver.execute_script("""
                const elem = arguments[0];
                const rect = elem.getBoundingClientRect();
                return (
                    rect.top >= 0 &&
                    rect.left >= 0 &&
                    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
                );
            """, element)

            if not is_in_viewport:
                # Scroll to the element
                self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'instant', block: 'center' });",
                                           element)

            return element

        except TimeoutException:
            raise AssertionError(f"The element {locator} did not appear in the span of {timeout} seconds.")

    def keyboard_navigation_tab(self, number_of_tabs:int):
        actions = ActionChains(self.driver)
        for _ in range(int(number_of_tabs)):
            actions.send_keys(Keys.TAB)
            time.sleep(0.1)
        actions.perform()

        time.sleep(0.5)

    def keyboard_access_element(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()

        time.sleep(0.5)

    def keyboard_navigation_arrow_down(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()

        time.sleep(0.5)

    def keyboard_navigation_arrow_up(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_UP)
        actions.perform()

        time.sleep(0.5)

    def assert_url(self, path: str) -> None:
        expected_url = URLS[path]
        try:
            WebDriverWait(self.driver, timeout=6, poll_frequency=0.1).until(EC.url_to_be(expected_url))
        except TimeoutException:
            current_url = self.driver.current_url
            raise AssertionError(f"Timeout waiting for exact URL '{expected_url}'. Current URL: '{current_url}'")

    def assert_url_negative(self, path: str) -> None:
        expected_url = URLS[path]
        try:
            WebDriverWait(self.driver, timeout=5).until(EC.url_contains(expected_url))
            raise AssertionError(f"Did NOT expect to go to'{expected_url}', but URL changed.")
        except TimeoutException:
            current_url = self.driver.current_url
            assert expected_url not in current_url, (
                f"Expected URL not to contain '{expected_url}', but it contained '{current_url}'"
            )

    def is_element_not_in_dom(self, locator):
        try:
            self.driver.find_element(*locator)
            return False
        except NoSuchElementException:
            return True

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def verify_element_removed_and_empty_state_displayed(self, removed_locator, expected_locator):
        # Verifies that element was removed from DOM
        try:
            self.driver.find_element(*removed_locator)
            assert False, f"Expected element {removed_locator} to not be present in dom, but it was found."
        except NoSuchElementException:
            pass

        # Verifies that text or another element IS present in DOM
        try:
            self.driver.find_element(*expected_locator)
        except NoSuchElementException:
            assert False, f"Expected element {expected_locator} to be present in dom, but it wasn't found."
