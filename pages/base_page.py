import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.config import URLS

class BasePage:
    def __init__(self, driver) -> None:
        self.driver = driver

    def visit(self, url: str) -> None:
        self.driver.get(url)

    # def visit(self, url:str) -> None:
    #     self.driver.get(URLS[url])



    # def click(self, locator: tuple[By, str]):
    #     self.driver.find_element(*locator).click()

    def click(self, locator: tuple[By, str], timeout=10):
        # Espera hasta que el elemento sea clickeable
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def type(self, locator: tuple[By, str], text: str):
        element = self.driver.find_element(*locator)
        element.clear()
        self.driver.find_element(*locator).send_keys(text)

    def text_of_element(self, locator: tuple[By, str]) -> str:
        return self.driver.find_element(*locator).text

    def assert_text_of_element(self, locator: tuple[By, str],expected_text: str):
        current_text = self.driver.find_element(*locator).text
        assert current_text == expected_text, f"Expected '{expected_text}', but got '{current_text}'"

    def element_is_visible(self, locator: tuple[By, str]) -> bool:
        return self.driver.find_element(*locator).is_displayed()


    # def element_is_clickable(self, locator: tuple[By, str], timeout=10) -> bool:
    #     try:
    #         WebDriverWait(self.driver, timeout).until(
    #             EC.element_to_be_clickable(*locator)
    #         )
    #         return True
    #     except:
    #         return False


    def hover(self, locator: tuple[By, str]):
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).perform()

    # def element_is_visible(self, locator, timeout=5):
    #     #print(f"Esperando visibilidad de: {locator}")
    #     return WebDriverWait(self.driver, timeout).until(
    #         EC.visibility_of_element_located(locator)
    #     )

    # def wait_until_invisible(self, locator, timeout=10) -> bool:
    #     try:
    #         WebDriverWait(self.driver, timeout, poll_frequency=0.1).until(
    #             EC.invisibility_of_element_located(locator)
    #         )
    #         return True
    #     except:
    #         return False

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

    def wait_until_visible(self, locator, timeout=5): # espera a que aparezca un elemento
        try:
            WebDriverWait(self.driver, timeout, poll_frequency=0.1).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"The element {locator} did not apper in the span of {timeout} seconds.")



    def move_pointer(self, locator1: tuple[By, str],xoffset: int, yoffset: int):
        element = self.driver.find_element(*locator1)
        ActionChains(self.driver).move_to_element(element).perform()
        ActionChains(self.driver).move_by_offset(xoffset, yoffset).perform()
        ActionChains(self.driver).click().perform()


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

    def assert_url(self, path:str) -> None:
        expected_url = URLS[path]
        WebDriverWait(self.driver, 5).until(
            EC.url_contains(expected_url)
        )
        current_url = self.driver.current_url
        assert current_url == expected_url, f"Expected {expected_url} but got {current_url}"


# probar, es para validar orden de links en el dom
    def test_order_of_links(driver):
        link1 = driver.find_element(By.ID, "link1")
        link2 = driver.find_element(By.ID, "link2")

        # Comparar posiciones en el DOM
        elements = driver.find_elements(By.TAG_NAME, "a")
        link_ids_in_order = [el.get_attribute("id") for el in elements]

        assert link_ids_in_order.index("link1") < link_ids_in_order.index("link2"), \
            "El link1 no está antes que link2 en el DOM"


    #def assert_inventory_url(self): #en realidad tiene que ir a la web de productos
    #    assert "inventory" in driver.current_url, "No te encuentras en URL /inventory" #valida que la palabra inventory esta en la URL