import pytest
from UI_project.utils.driver_factory import create_driver
import os
from datetime import datetime
import logging
from pytest_html import extras
import base64

def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run in headless mode",
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox", "edge"],
        help="Choose between chrome, firefox, edge browsers",
    )

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = create_driver(browser=browser, headless=headless)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshot_dir = os.path.join("UI_project", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name.replace("/", "_")
            filename = f"{test_name}_{timestamp}.png"
            filepath = os.path.join(screenshot_dir, filename)

            driver.save_screenshot(filepath)
            print(f"Screenshot saved: {filepath}")

            with open(filepath, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

            image_extra = extras.image(encoded_image, mime_type='image/png')

            if hasattr(rep, "extra"):
                rep.extras.append(image_extra)
            else:
                rep.extras = [image_extra]

def pytest_configure(config):
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")