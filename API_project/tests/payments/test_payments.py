import pytest, datetime, time
from jsonschema import validate
import pytest_check as check
from API_project.tests.airports.test_schema import good_airport_data
from API_project.tests.bookings.conftest import bad_passenger_data
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS, USERS_ME
from API_project.utils.fixture_utils import auth_headers
from API_project.utils.api_helpers import api_request
from API_project.tests.airports.conftest import create_clear_airport_1, create_clear_airport_2
from API_project.tests.aircrafts.conftest import create_clear_aircraft
from API_project.tests.bookings.conftest import passenger_data
from API_project.tests.airports.test_schema import good_airport_data_1, good_airport_data_2
from API_project.tests.aircrafts.test_schema import good_aircraft_data
from API_project.tests.bookings.test_schema import booking_schema, booking_schema_array, bad_booking_passenger_data, random_booking_passenger_data
from API_project.tests.payments.test_schema import bad_payment_amount_method_data, payment_schema, payment_schema_array

@pytest.mark.api
@pytest.mark.happy_path_flow
@pytest.mark.parametrize('airport_data_1, airport_data_2, aircraft_data', [(good_airport_data_1, good_airport_data_2, good_aircraft_data)])
def test_create_get_payment(create_payment, auth_headers):
    payment_data, payment_creation_status_code, payment_creation_json = create_payment
    validate(instance=payment_creation_json, schema=payment_schema)
    payment_id = payment_creation_json["id"]

    get_payment = api_request(method="GET", path=f"{PAYMENTS}/{payment_id}", headers=auth_headers)
    get_payment_json = get_payment.json()

    check.equal(get_payment_json['booking_id'], payment_data['booking_id'], "Booking id mismatch")
    assert "id" in get_payment_json
    assert "status" in get_payment_json

@pytest.mark.api
@pytest.mark.fail
@pytest.mark.parametrize('airport_data_1', [good_airport_data_1])
@pytest.mark.parametrize('airport_data_2', [good_airport_data_2])
@pytest.mark.parametrize('aircraft_data', [good_aircraft_data])
@pytest.mark.parametrize('bad_payment_amount_method_data', bad_payment_amount_method_data)
def test_create_payment_fail_negative_flow(create_payment_negative, auth_headers):
    payment_data = create_payment_negative
    payment_creation = api_request(method="POST", path=PAYMENTS, json=payment_data, headers=auth_headers)
    bad_payment_creation_status_code = payment_creation.status_code

    assert bad_payment_creation_status_code in (400, 422), f"Expected 400 or 422, got {bad_payment_creation_status_code}, for payment data {create_payment_negative}. This suggests the API accepted payment data with non valid or missing data, or failed to return the correct validation error."

@pytest.mark.api
@pytest.mark.fail
@pytest.mark.parametrize('airport_data_1, airport_data_2, aircraft_data', [(good_airport_data_1, good_airport_data_2, good_aircraft_data)])
def test_create_get_payment_deleted_booking(create_payment_deleted_booking, auth_headers):
    payment_data, payment_creation_status_code = create_payment_deleted_booking
    assert payment_creation_status_code == 422, f"Expected 422, got {payment_creation_status_code}. This suggests the API accepted a payment with a non-existent booking ID, or failed to return the correct validation error."

@pytest.mark.api
@pytest.mark.fail
@pytest.mark.parametrize('airport_data_1, airport_data_2, aircraft_data', [(good_airport_data_1, good_airport_data_2, good_aircraft_data)])
def test_create_payment_not_authenticated(create_payment_fail_not_authenticated):
    payment_creation_status_code = create_payment_fail_not_authenticated
    assert payment_creation_status_code in (401, 403), f"Expected 401 or 403, got {payment_creation_status_code}. This suggests the API accepted a payment request without authentication, or failed to return the correct validation error."

