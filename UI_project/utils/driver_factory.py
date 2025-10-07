from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def create_driver(browser="chrome", headless=False):
    browser = browser.lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument('--incognito')

        if headless:
            options.add_argument("--headless=new")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options,
        )

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--private")
        if headless:
            options.add_argument("--headless")

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

    elif browser == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--inprivate")
        if headless:
            options.add_argument("--headless=new")

        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options
        )

    else:
        raise ValueError(f"Browser not supported: {browser}")

    driver.implicitly_wait(5)
    return driver

