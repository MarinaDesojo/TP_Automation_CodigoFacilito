import datetime, random, requests, string
import pytest, time
from API_project.utils.api_helpers import api_request
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS, USERS_ME
from API_project.utils.fixture_utils import admin_token, auth_headers
from API_project.tests.airports.conftest import create_clear_airport_1, create_clear_airport_2
from API_project.tests.aircrafts.conftest import create_clear_aircraft
from API_project.tests.airports.test_schema import good_airport_data_1, good_airport_data_2
from API_project.tests.aircrafts.test_schema import good_aircraft_data
from API_project.tests.flights.test_schema import flight_schema, flight_schema_array, random_flight_data, bad_flight_scenarios

@pytest.fixture
def create_clear_flight(create_clear_airport_1, create_clear_airport_2, create_clear_aircraft, auth_headers):
    origin = create_clear_airport_1.get("iata_code")
    destination = create_clear_airport_2.get("iata_code")
    aircraft_id = create_clear_aircraft.get("id")

    departure = fake.date_time(tzinfo=datetime.timezone.utc)
    arrival = departure + datetime.timedelta(hours=5)

    flight_data = {
        "origin": origin,
        "destination": destination,
        "departure_time": departure.isoformat().replace('+00:00', 'Z'),
        "arrival_time": arrival.isoformat().replace('+00:00', 'Z'),
        "base_price": round(fake.pyfloat(left_digits=3,  right_digits=2, positive=True), 2),
        "aircraft_id": aircraft_id
    }

    flight_creation = api_request(method="POST", path=FLIGHTS, json=flight_data, headers=auth_headers)
    flight_creation_json = flight_creation.json()

    yield flight_data, flight_creation_json

    flight_id = flight_creation_json["id"]
    MAX_RETRIES = 3
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            api_request(method="DELETE", path=f"{FLIGHTS}/{flight_id}", headers=auth_headers)
            get_flight_after_delete = api_request(method="GET", path=f"{FLIGHTS}/{flight_id}", headers=auth_headers)
            if get_flight_after_delete.status_code in (404, 422):
                print("Flight deleted successfully")
                break
            else:
                print (f"Flight still exists, status {get_flight_after_delete.status_code}, retrying delete")
        except Exception as e:
            print (f"Error during request {e}")
    else:
        raise Exception(f"Flight was not deleted after {MAX_RETRIES} attempts")

@pytest.fixture
def get_all_flights(auth_headers, limit=50):
    skip = 0
    results = []
    while True:
        r = api_request(method="GET", path=FLIGHTS, headers=auth_headers, params={"skip": skip, "limit": limit})
        r.raise_for_status()
        flights_list = r.json()
        if not flights_list:
            break
        results.extend(flights_list)
        skip += limit
    return results

@pytest.fixture
def create_clear_flight_negative(create_clear_airport_1, create_clear_airport_2, create_clear_aircraft, bad_flight_scenarios, auth_headers):
    origin = create_clear_airport_1.get("iata_code")
    destination = create_clear_airport_2.get("iata_code")
    aircraft_id = create_clear_aircraft.get("id")

    bad_flight_data = {
        "origin": origin,
        "destination": destination,
        "departure_time": bad_flight_scenarios["departure_time"],
        "arrival_time": bad_flight_scenarios["arrival_time"],
        "base_price": bad_flight_scenarios["base_price"],
        "aircraft_id": aircraft_id
    }

    flight_creation = api_request(method="POST", path=FLIGHTS, json=bad_flight_data, headers=auth_headers)
    flight_creation_json = flight_creation.json()
    bad_flight_creation_status_code = flight_creation.status_code

    yield bad_flight_data, bad_flight_creation_status_code, flight_creation_json

    flight_id = flight_creation_json["id"]
    retries = 3

    try:
        for attempt in range(retries):
            api_request(method="DELETE", path=f"{FLIGHTS}/{flight_id}", headers=auth_headers)
            get_flight_after_delete = api_request(method="GET", path=f"{FLIGHTS}/{flight_id}", headers=auth_headers)
            if get_flight_after_delete.status_code in (404, 422):
                print("Flight deleted successfully")
                break
            else:
                print (f"Flight still exists, status {get_flight_after_delete.status_code}, retrying delete")
                time.sleep(1)
        else:
            print(f"Warning: Failed to delete flight {flight_id} after {retries} attempts")
    except Exception as e:
        print(f"Exception during cleanup: {e}")

@pytest.fixture
def flight_variable_path_teardown(auth_headers):
    resources = []
    yield resources
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
def create_clear_flight_fail_not_authenticated(create_clear_airport_1, create_clear_airport_2, create_clear_aircraft, auth_headers):
    origin = create_clear_airport_1.get("iata_code")
    destination = create_clear_airport_2.get("iata_code")
    aircraft_id = create_clear_aircraft.get("id")

    departure = fake.date_time(tzinfo=datetime.timezone.utc)
    arrival = departure + datetime.timedelta(hours=5)

    flight_data = {
        "origin": origin,
        "destination": destination,
        "departure_time": departure.isoformat().replace('+00:00', 'Z'),
        "arrival_time": arrival.isoformat().replace('+00:00', 'Z'),
        "base_price": round(fake.pyfloat(left_digits=3,  right_digits=2, positive=True), 2),
        "aircraft_id": aircraft_id
    }

    flight_creation = api_request(method="POST", path=FLIGHTS, json=flight_data)
    flight_creation_status_code = flight_creation.status_code

    yield flight_data, flight_creation_status_code

    MAX_RETRIES = 3
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            flight_id = flight_creation.json().get("id")
            api_request(method="DELETE", path=f"{FLIGHTS}/{flight_id}", headers=auth_headers)
            get_flight_after_delete = api_request(method="GET", path=f"{FLIGHTS}/{flight_id}", headers=auth_headers)
            if get_flight_after_delete.status_code in (404, 422):
                print("Flight deleted successfully")
                break
            else:
                print (f"Flight still exists, status {get_flight_after_delete.status_code}, retrying delete")
        except Exception as e:
            print (f"Error during request {e}")
    else:
        raise Exception(f"Flight was not deleted after {MAX_RETRIES} attempts")

