import pytest
from utils.driver_factory import create_driver
import os
from datetime import datetime

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

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshot_dir = "UI_project/tests/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name.replace("/", "_")
            screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")
            driver.save_screenshot(screenshot_path)
            print(f"\n Screenshot saved: {screenshot_path}")

            # Para pytest-html
            extra = getattr(rep, "extra", [])
            if item.config.pluginmanager.hasplugin("html"):
                from pytest_html import extras
                extra.append(extras.image(screenshot_path))
                rep.extra = extra
