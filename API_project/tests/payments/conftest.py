import datetime, random, requests, string
import pytest, time
from API_project.utils.api_helpers import api_request
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS, USERS_ME
from API_project.utils.fixture_utils import admin_token, auth_headers
from API_project.tests.airports.conftest import create_clear_airport_1, create_clear_airport_2
from API_project.tests.aircrafts.conftest import create_clear_aircraft
from API_project.tests.users.conftest import create_clear_user
from API_project.tests.flights.conftest import create_clear_flight
from API_project.tests.bookings.test_schema import random_booking_passenger_data, bad_booking_passenger_data, good_booking_passenger_data
from API_project.tests.flights.test_schema import flight_schema, flight_schema_array, random_flight_data, bad_flight_scenarios
from API_project.tests.bookings.conftest import create_clear_booking
from API_project.tests.payments.test_schema import bad_payment_amount_method_data

@pytest.fixture
def payment_data(create_clear_booking, auth_headers):
    booking_data, booking_creation_json = create_clear_booking
    booking_id = booking_creation_json["id"]


    payment_data = {
        "booking_id": booking_id,
        "amount": 0,
        "payment_method": ""
    }

    return payment_data

@pytest.fixture
def create_payment(payment_data, auth_headers):
    payment_creation = api_request(method="POST", path=PAYMENTS, json=payment_data, headers=auth_headers)
    payment_creation_status_code = payment_creation.status_code
    payment_creation_json = payment_creation.json()

    return payment_data, payment_creation_status_code, payment_creation_json

@pytest.fixture
def create_payment_negative(create_clear_booking, bad_payment_amount_method_data, auth_headers):
    booking_data, booking_creation_json = create_clear_booking
    booking_id = booking_creation_json["id"]

    bad_payment_data = {
        "booking_id": booking_id,
        "amount": bad_payment_amount_method_data["amount"],
        "payment_method": bad_payment_amount_method_data["payment_method"]
    }

    return bad_payment_data

@pytest.fixture
def create_payment_deleted_booking(payment_data, auth_headers):
    api_request(method="DELETE", path=f"{BOOKINGS}/{payment_data['booking_id'], auth_headers}")
    get_deleted_booking = api_request(method="GET", path=f"{BOOKINGS}/{payment_data['booking_id'], auth_headers}")
    assert get_deleted_booking == 422, f"Expected 422, got {get_deleted_booking}, This suggests the API did not delete the booking ID, or failed to return the correct validation error."

    payment_creation = api_request(method="POST", path=PAYMENTS, json=payment_data, headers=auth_headers)
    payment_creation_status_code = payment_creation.status_code

    return payment_data, payment_creation_status_code

@pytest.fixture
def create_payment_fail_not_authenticated(payment_data, auth_headers):
    payment_creation = api_request(method="POST", path=PAYMENTS, json=payment_data)
    payment_creation_status_code = payment_creation.status_code

    return payment_creation_status_code
