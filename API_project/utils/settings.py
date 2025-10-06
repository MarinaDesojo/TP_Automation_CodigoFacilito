# Endpoints and faker
from dotenv import load_dotenv
import os
import faker
from pathlib import Path
load_dotenv(Path(__file__).parent / ".env")

BASE_URL = os.getenv("BASE_URL")
fake = faker.Faker()

AUTH_LOGIN = "/auth/login"
USERS = "/users"
USERS_ME = "/users/me"
AIRPORTS = "/airports"
FLIGHTS = "/flights"
BOOKINGS = "/bookings"
PAYMENTS = "/payments"
AIRCRAFTS = "/aircrafts"




