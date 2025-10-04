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
from API_project.tests.airports.test_schema import good_airport_data_1, good_airport_data_2
from API_project.tests.aircrafts.test_schema import good_aircraft_data
from API_project.tests.bookings.test_schema import booking_schema, booking_schema_array, bad_booking_passenger_data, random_booking_passenger_data
from API_project.tests.users.test_schema import good_user_data

@pytest.mark.parametrize('airport_data_1, airport_data_2, aircraft_data', [(good_airport_data_1, good_airport_data_2, good_aircraft_data)])
def test_create_clear_booking(create_clear_booking, auth_headers):
    booking_data, booking_creation_json = create_clear_booking
    validate(instance=booking_creation_json, schema=booking_schema)
    booking_id = booking_creation_json["id"]

    get_booking = api_request(method="GET", path=f"{BOOKINGS}/{booking_id}", headers=auth_headers)
    booking_json = get_booking.json()

    for i, passenger in enumerate(booking_json["passengers"]):
        passenger_data = booking_data["passengers"][i]
        check.equal(passenger["full_name"], passenger_data["full_name"], f"Full name mismatch for passenger {i}")
        check.equal(passenger["passport"], passenger_data["passport"], f"Passport mismatch for passenger {i}")
        check.equal(passenger["seat"], passenger_data["seat"], f"Seat mismatch for passenger {i}")


@pytest.mark.parametrize('airport_data_1, airport_data_2, aircraft_data', [(good_airport_data_1, good_airport_data_2, good_aircraft_data)])
def test_create_clear_booking_fail_negative_flow(create_clear_booking_negative, auth_headers):
    bad_booking_data, bad_booking_creation_status_code, booking_creation_json = create_clear_booking_negative
    assert bad_booking_creation_status_code in (400, 422), f"Expected 400 or 422, got {bad_booking_creation_status_code}"

    try:
        booking_id = booking_creation_json.get("id")
    except Exception:
        booking_id = None

    if booking_id:
        get_resp = api_request(method="GET", path=f"{BOOKINGS}/{booking_id}", headers=auth_headers)
        if get_resp.status_code in (200, 204):
            print(f"Warning, booking was created despite receiving status {get_resp.status_code} for: {booking_id}")
            delete_resp = api_request(method="DELETE", path=f"{BOOKINGS}/{booking_id}", headers=auth_headers)
            if delete_resp.status_code != 204:
                print(f"Warning: Failed to delete booking {booking_id}")

# doble booking con exactamente la misma data, no debería permitirlo

@pytest.mark.parametrize('airport_data_1, airport_data_2, aircraft_data', [(good_airport_data_1, good_airport_data_2, good_aircraft_data)])
def test_double_create_clear_booking(create_clear_booking, auth_headers):
    booking_data, booking_creation_json = create_clear_booking
    # validate(instance=booking_creation_json, schema=booking_schema)

    booking_double_creation = api_request(method="POST", path=BOOKINGS, json=booking_data, headers=auth_headers)
    assert booking_double_creation.status_code in (409, 422), f"Expected 409 or 422, got {booking_double_creation.status_code}"


# Fail, creí que sumaba los passenger de 2 bookings pero no funciona así, hace un booking con su propio id cada uno

# @pytest.mark.parametrize('airport_data_1, airport_data_2, aircraft_data',[(good_airport_data_1, good_airport_data_2, good_aircraft_data)])
# def test_double_create_clear_booking_different_data(create_clear_booking, auth_headers):
#     booking_data, booking_creation_json = create_clear_booking
#     validate(instance=booking_creation_json, schema=booking_schema)
#     booking_id = booking_creation_json["id"]
#
#     import random
#
#     second_booking_data = {
#         "flight_id": booking_data["flight_id"],
#         "passengers": [
#             {
#                 "full_name": fake.name(),
#                 "passport": fake.bothify(text='??######'),
#                 "seat": f"{random.randint(1, 60)}{random.choice(['A', 'B', 'C', 'D', 'E', 'F'])}"
#             }
#         ],
#         "additionalProperties": False
#     }
#
#     booking_double_creation = api_request(method="POST", path=BOOKINGS, json=second_booking_data, headers=auth_headers)
#     assert booking_double_creation.status_code == 201, f"Expected 201, got {booking_double_creation.status_code}"
#     booking_double_creation_json = booking_double_creation.json()
#     booking_double_creation_id = booking_double_creation_json["id"]
#
#     get_first_booking = api_request(method="GET", path=f"{BOOKINGS}/{booking_id}", headers=auth_headers)
#     get_first_booking_json = get_first_booking.json()
#
#     get_second_booking = api_request(method="GET", path=f"{BOOKINGS}/{booking_double_creation_id}", headers=auth_headers)
#     get_second_booking_json = get_second_booking.json()
#
#     for i, passenger_first_booking in enumerate(get_first_booking_json["passengers"]):
#         passenger_data_first_booking = booking_data["passengers"][i]
#         check.equal(passenger_first_booking["full_name"], passenger_data_first_booking["full_name"], f"Full name mismatch for passenger {i}")
#         check.equal(passenger_first_booking["passport"], passenger_data_first_booking["passport"], f"Passport mismatch for passenger {i}")
#         check.equal(passenger_first_booking["seat"], passenger_data_first_booking["seat"], f"Seat mismatch for passenger {i}")
#
#     for i, passenger_second_booking in enumerate(get_second_booking_json["passengers"]):
#         passenger_data_second_booking = second_booking_data["passengers"][i]
#         check.equal(passenger_second_booking["full_name"], passenger_data_second_booking["full_name"], f"Full name mismatch for passenger {i}")
#         check.equal(passenger_second_booking["passport"], passenger_data_second_booking["passport"], f"Passport mismatch for passenger {i}")
#         check.equal(passenger_second_booking["seat"], passenger_data_second_booking["seat"], f"Seat mismatch for passenger {i}")


@pytest.mark.parametrize('airport_data_1, airport_data_2, aircraft_data',[(good_airport_data_1, good_airport_data_2, good_aircraft_data)])
def test_update_bookingt(create_clear_booking, auth_headers):
    booking_data, booking_creation_json = create_clear_booking
    booking_id = booking_creation_json["id"]

    changed_booking_data = {
                "flight_id": booking_data["flight_id"],
                "passengers": [
                    {
                        "full_name": "Carlos Gonzalez",
                        "passport": "AS165452135",
                        "seat": "G28"
                    }
                ],
                "additionalProperties": False
            }
    update_booking = api_request(method="PATCH", path=f"{BOOKINGS}/{booking_id}", json=changed_booking_data, headers=auth_headers)
    update_booking.raise_for_status()

    get_updated_booking = api_request(method="GET", path=f"{BOOKINGS}/{booking_id}", headers=auth_headers)
    updated_booking_json = get_updated_booking.json()

    check.equal(updated_booking_json['flight_id'], changed_booking_data['flight_id'], "Origin iata code mismatch")
    for i, passenger in enumerate(updated_booking_json["passengers"]):
        passenger_data = changed_booking_data["passengers"][i]
        check.equal(passenger["full_name"], passenger_data["full_name"], f"Full name mismatch for passenger {i}")
        check.equal(passenger["passport"], passenger_data["passport"], f"Passport mismatch for passenger {i}")
        check.equal(passenger["seat"], passenger_data["seat"], f"Seat mismatch for passenger {i}")



@pytest.mark.parametrize('airport_data_1, airport_data_2, aircraft_data',[(good_airport_data_1, good_airport_data_2, good_aircraft_data)])
def test_get_all_bookings(create_clear_booking, get_all_bookings, auth_headers):
    validate(instance=get_all_bookings, schema=booking_schema_array)


@pytest.mark.parametrize('airport_data_1, airport_data_2, aircraft_data',[(good_airport_data_1, good_airport_data_2, good_aircraft_data)])
def test_booking_deleted_data_flight(passenger_data, bookings_variable_path_teardown, auth_headers):
    resources, flight_id = bookings_variable_path_teardown
    api_request(method="DELETE", path=f"{FLIGHTS}/{flight_id}", headers=auth_headers)

    booking_data = {
        "flight_id": flight_id,
        "passengers": passenger_data,
        "additionalProperties": False
    }

    booking_creation = api_request(method="POST", path=BOOKINGS, json=booking_data, headers=auth_headers)
    if booking_creation.status_code in (200, 201):
        booking_creation_json = booking_creation.json()
        booking_id = booking_creation_json["id"]
        resources.append({"path": f"{BOOKINGS}/{booking_id}"})
    assert booking_creation.status_code == 422, f"Expected 422, got {booking_creation.status_code}. This suggests the API accepted a booking with a non-existent flight ID, or failed to return the correct validation error."


@pytest.mark.parametrize('airport_data_1, airport_data_2, aircraft_data',[(good_airport_data_1, good_airport_data_2, good_aircraft_data)])
def test_booking_empty_data_flight(passenger_data, bookings_variable_path_teardown, auth_headers):
    resources, flight_id = bookings_variable_path_teardown

    booking_data = {
        "flight_id": "",
        "passengers": passenger_data,
        "additionalProperties": False
    }

    booking_creation = api_request(method="POST", path=BOOKINGS, json=booking_data, headers=auth_headers)
    if booking_creation.status_code in (200, 201):
        booking_creation_json = booking_creation.json()
        booking_id = booking_creation_json["id"]
        resources.append({"path": f"{BOOKINGS}/{booking_id}"})
    assert booking_creation.status_code == 422, f"Expected 422, got {booking_creation.status_code}. This suggests the API accepted a booking with an empty flight ID, or failed to return the correct validation error."


@pytest.mark.parametrize('airport_data_1, airport_data_2, aircraft_data',[(good_airport_data_1, good_airport_data_2, good_aircraft_data)])
def test_booking_empty_data_passenger(bookings_variable_path_teardown, auth_headers):
    resources, flight_id = bookings_variable_path_teardown

    booking_data = {
        "flight_id": flight_id,
        "passengers": [],
        "additionalProperties": False
    }

    booking_creation = api_request(method="POST", path=BOOKINGS, json=booking_data, headers=auth_headers)
    if booking_creation.status_code == 201:
        booking_creation_json = booking_creation.json()
        booking_id = booking_creation_json["id"]
        resources.append({"path": f"{BOOKINGS}/{booking_id}"})
    assert booking_creation.status_code == 422, f"Expected 422, got {booking_creation.status_code}. This suggests the API accepted a booking with an empty list of passengers, or failed to return the correct validation error."


@pytest.mark.parametrize('airport_data_1, airport_data_2, aircraft_data',[(good_airport_data_1, good_airport_data_2, good_aircraft_data)])
def test_booking_string_data_passenger(bookings_variable_path_teardown, auth_headers):
    resources, flight_id = bookings_variable_path_teardown

    booking_data = {
        "flight_id": flight_id,
        "passengers": "",
        "additionalProperties": False
    }

    booking_creation = api_request(method="POST", path=BOOKINGS, json=booking_data, headers=auth_headers)
    assert booking_creation.status_code == 422, f"Expected 422, got {booking_creation.status_code}. This suggests the API accepted a booking with a string instead of a list of passengers, or failed to return the correct validation error."
    if booking_creation.status_code == 201:
        booking_creation_json = booking_creation.json()
        booking_id = booking_creation_json["id"]
        resources.append({"path": f"{BOOKINGS}/{booking_id}"})

