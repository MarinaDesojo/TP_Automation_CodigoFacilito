#para que sirve? para contener los metodos genericos que van a estar presentes en todos los page objects
#desde escribir, a hacer click, obtener un dato, etc, y se puede actualizar desde aca para actualizartodo lode mas

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:


    def __init__(self, driver) -> None:
        self.driver = driver

    def visit(self, url: str) -> None:
        self.driver.get(url)

    # def click(self, locator: tuple[By, str]):
    #     self.driver.find_element(*locator).click()

    def click(self, locator: tuple[By, str], timeout=10):
        # Espera hasta que el elemento sea clickeable
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)  # ✅ solo un argumento
        )
        element.click()

    def type(self, locator: tuple[By, str], text: str):
        element = self.driver.find_element(*locator)
        element.clear()
        self.driver.find_element(*locator).send_keys(text)

    def text_of_element(self, locator: tuple[By, str]) -> str:
        return self.driver.find_element(*locator).text

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

    def wait_until_invisible(self, locator, timeout=10) -> bool:
        try:
            WebDriverWait(self.driver, timeout, poll_frequency=0.1).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except:
            return False
