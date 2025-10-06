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

@pytest.fixture(params=[random_booking_passenger_data])
def passenger_data(request):
    return request.param

@pytest.fixture
def create_clear_booking(create_clear_flight, passenger_data, auth_headers):
    flight_data, flight_creation_json = create_clear_flight
    flight_id = flight_creation_json["id"]


    booking_data = {
        "flight_id": flight_id,
        "passengers": passenger_data,
        "additionalProperties": False
    }

    booking_creation = api_request(method="POST", path=BOOKINGS, json=booking_data, headers=auth_headers)
    booking_creation_json = booking_creation.json()

    yield booking_data, booking_creation_json

    booking_id = booking_creation_json["id"]
    MAX_RETRIES = 3
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            api_request(method="DELETE", path=f"{BOOKINGS}/{booking_id}", headers=auth_headers)
            get_booking_after_delete = api_request(method="GET", path=f"{BOOKINGS}/{booking_id}", headers=auth_headers)
            if get_booking_after_delete.status_code in (404, 422):
                print("Booking deleted successfully")
                break
            else:
                print (f"Booking code {booking_id} still exists, get status {get_booking_after_delete.status_code}, retrying delete")
        except Exception as e:
            print (f"Error during request {e}")
    else:
        raise Exception(f"Booking code {booking_id} was not deleted after {MAX_RETRIES} attempts")

@pytest.fixture
def get_all_bookings(auth_headers, limit=50):
    skip = 0
    results = []
    while True:
        r = api_request(method="GET", path=BOOKINGS, headers=auth_headers, params={"skip": skip, "limit": limit})
        r.raise_for_status()
        flights_list = r.json()
        if not flights_list:
            break
        results.extend(flights_list)
        skip += limit
    return results

@pytest.fixture(params=bad_booking_passenger_data, ids=[f"case_{i}" for i in range(len(bad_booking_passenger_data))])
def bad_passenger_data(request):
    return request.param

@pytest.fixture
def create_clear_booking_negative(create_clear_flight, bad_passenger_data, auth_headers):
    flight_data, flight_creation_json = create_clear_flight
    flight_id = flight_creation_json["id"]

    bad_booking_data = {
        "flight_id": flight_id,
        "passengers": bad_passenger_data,
        "additionalProperties": False
    }

    booking_creation = api_request(method="POST", path=BOOKINGS, json=bad_booking_data, headers=auth_headers)
    booking_creation_json = booking_creation.json()
    bad_booking_creation_status_code = booking_creation.status_code

    yield bad_booking_data, bad_booking_creation_status_code, booking_creation_json

    booking_id = booking_creation_json["id"]
    MAX_RETRIES = 3
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            api_request(method="DELETE", path=f"{BOOKINGS}/{booking_id}", headers=auth_headers)
            get_booking_after_delete = api_request(method="GET", path=f"{BOOKINGS}/{booking_id}", headers=auth_headers)
            if get_booking_after_delete.status_code in (404, 422):
                print("Booking deleted successfully")
                break
            else:
                print (f"Booking code {booking_id} still exists, get status {get_booking_after_delete.status_code}, retrying delete")
        except Exception as e:
            print (f"Error during request {e}")
    else:
        raise Exception(f"Booking code {booking_id} was not deleted after {MAX_RETRIES} attempts")

@pytest.fixture
def bookings_variable_path_teardown(create_clear_flight, passenger_data, auth_headers):
    flight_data, flight_creation_json = create_clear_flight
    flight_id = flight_creation_json["id"]

    resources = []
    yield resources, flight_id
    MAX_RETRIES = 3
    for resource in resources:
        path = resource["path"]
        verify_path = resource.get("verify_path", path)
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                api_request(method="DELETE", path=path, headers=auth_headers)
                get_response_after_delete = api_request(method="GET", path=verify_path, headers=auth_headers)
                if get_response_after_delete.status_code in (404, 422):
                    print(f"Resource at {path} deleted successfully")
                    break
                else:
                    print(f"Resource at {path} still exists, status {get_response_after_delete.status_code}, retrying delete")
            except Exception as e:
                print(f"Error during request {e}")
        else:
            raise Exception(f"Resource at {path} was not deleted after {MAX_RETRIES} attempts")

@pytest.fixture
def create_clear_booking_fail_not_authenticated(create_clear_flight, passenger_data, auth_headers):
    flight_data, flight_creation_json = create_clear_flight
    flight_id = flight_creation_json["id"]


    booking_data = {
        "flight_id": flight_id,
        "passengers": passenger_data,
        "additionalProperties": False
    }

    booking_creation = api_request(method="POST", path=BOOKINGS, json=booking_data)
    booking_creation_status_code = booking_creation.status_code

    yield booking_data, booking_creation_status_code

    MAX_RETRIES = 3
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            booking_creation_json = booking_creation.json()
            booking_id = booking_creation_json["id"]
            api_request(method="DELETE", path=f"{BOOKINGS}/{booking_id}", headers=auth_headers)
            get_booking_after_delete = api_request(method="GET", path=f"{BOOKINGS}/{booking_id}", headers=auth_headers)
            if get_booking_after_delete.status_code in (404, 422):
                print("Booking deleted successfully")
                break
            else:
                print (f"Booking code {booking_id} still exists, get status {get_booking_after_delete.status_code}, retrying delete")
        except Exception as e:
            print (f"Error during request {e}")
    else:
        raise Exception(f"Booking code {booking_id} was not deleted after {MAX_RETRIES} attempts")

