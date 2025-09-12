from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import (By)

load_dotenv()

EMAIL_USER = os.getenv("TEST_EMAIL_USER")
PASSWORD = os.getenv("TEST_PASSWORD")
EMAIL_NO_AT = os.getenv("TEST_EMAIL_NO_AT")
EMAIL_NO_TEXT_POST_AT = os.getenv("TEST_EMAIL_NO_TEXT_POST_AT")
EMAIL_NO_TEXT_PRE_AT = os.getenv("TEST_EMAIL_NO_TEXT_PRE_AT")
EMAIL_ONLY_AT = os.getenv("@")
EMAIL_NO_DOT_COM = os.getenv("TEST_EMAIL_NO_DOT_COM")
FIRST_NAME = os.getenv("TEST_FIRST_NAME")
LAST_NAME = os.getenv("TEST_LAST_NAME")
ZIP_CODE = os.getenv("TEST_ZIP_CODE")
PHONE_NUMBER = os.getenv("TEST_PHONE_NUMBER")
ADDRESS = os.getenv("TEST_ADDRESS")
CITY = os.getenv("TEST_CITY")
COUNTRY = os.getenv("TEST_COUNTRY")

BASE_URL = "https://shophub-commerce.vercel.app/"
product_number = 1

URLS = {
    "homepage": BASE_URL,
    "books": f"{BASE_URL}categories/books",
    "cart": f"{BASE_URL}cart",
    "checkout": f"{BASE_URL}checkout",
    "confirmation": f"{BASE_URL}confirmation",
    "electronics": f"{BASE_URL}categories/electronics",
    "groceries": f"{BASE_URL}categories/groceries",
    "login": f"{BASE_URL}login",
    "logged_in": f"{BASE_URL}login/success",
    "men_clothes": f"{BASE_URL}categories/men-clothes",
    "signup": f"{BASE_URL}signup",
    "special_deals": f"{BASE_URL}categories/special-deals",
    "women_clothes": f"{BASE_URL}categories/women-clothes"
}

# Product details page (PDP) has a dynamic URL:
def get_product_url(product_number: str) -> str:
    return f"{BASE_URL}product/{product_number}"

LOADING_OVERLAY = (By.CSS_SELECTOR, 'div.fixed.inset-0.z-50.flex.items-center.justify-center.bg-background\\/70')