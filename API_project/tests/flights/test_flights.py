import pytest, datetime, time
from jsonschema import validate
import pytest_check as check

from API_project.tests.airports.test_schema import good_airport_data
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS, USERS_ME
from API_project.utils.fixture_utils import auth_headers
from API_project.utils.api_helpers import api_request
from API_project.tests.airports.conftest import create_clear_airport_1, create_clear_airport_2
from API_project.tests.aircrafts.conftest import create_clear_aircraft
from API_project.tests.airports.test_schema import good_airport_data_1, good_airport_data_2
from API_project.tests.aircrafts.test_schema import good_aircraft_data
from API_project.tests.flights.test_schema import flight_schema, flight_schema_array, random_flight_data, bad_flight_scenarios

@pytest.mark.parametrize('airport_data_1, airport_data_2, aircraft_data',[(good_airport_data_1, good_airport_data_2, good_aircraft_data)])
def test_create_clear_flight(create_clear_flight, auth_headers):
    flight_data, flight_creation_json = create_clear_flight
    validate(instance=flight_creation_json, schema=flight_schema)
    flight_id = flight_creation_json["id"]

    get_flight = api_request(method="GET", path=f"{FLIGHTS}/{flight_id}", headers=auth_headers)
    flight = get_flight.json()
    check.equal(flight['origin'], flight_data['origin'], "Origin iata code mismatch")
    check.equal(flight['destination'], flight_data['destination'], "Destination iata code mismatch")
    check.equal(flight['departure_time'], flight_data['departure_time'], "Departure time mismatch")
    check.equal(flight['arrival_time'], flight_data['arrival_time'], "Arrival time mismatch")
    check.equal(flight['base_price'], flight_data['base_price'], "Base price mismatch")
    check.equal(flight['aircraft_id'], flight_data['aircraft_id'], "Aircraft id mismatch")

@pytest.mark.parametrize('airport_data_1', [good_airport_data_1])
@pytest.mark.parametrize('airport_data_2', [good_airport_data_2])
@pytest.mark.parametrize('aircraft_data', [good_aircraft_data])
@pytest.mark.parametrize('bad_flight_scenarios', bad_flight_scenarios)
def test_create_clear_flight_fail_negative_flow(create_clear_flight_negative, auth_headers):
    bad_flight_data, bad_flight_creation_status_code, flight_creation_json = create_clear_flight_negative
    assert bad_flight_creation_status_code in (400, 422), f"Expected 400 or 422, got {bad_flight_creation_status_code}"

    flight_id = flight_creation_json.get('id')
    if flight_id:
        get_resp = api_request(method="GET", path=FLIGHTS, headers=auth_headers, params={"id": flight_id})
        aircrafts_found = get_resp.json()
        for aircraft in aircrafts_found:
            if aircraft.get('id') == flight_id:
                print(f"Warning, aircraft was created despite of {bad_flight_creation_status_code} for: {flight_id}")

                delete_resp = api_request(method="DELETE", path=f"{FLIGHTS}/{flight_id}",
                                          headers=auth_headers)
                if delete_resp.status_code != 204:
                    print(f"Warning: Failed to delete airport {flight_id}")



@pytest.mark.parametrize('airport_data_1, airport_data_2, aircraft_data',[(good_airport_data_1, good_airport_data_2, good_aircraft_data)])
def test_double_create_clear_flight(create_clear_flight, auth_headers):
    flight_data, flight_creation_json = create_clear_flight
    # validate(instance=flight_creation_json, schema=flight_schema)
    # flight_id = flight_creation_json["id"]
    #
    # get_flight = api_request(method="GET", path=f"{FLIGHTS}/{flight_id}", headers=auth_headers)
    # flight = get_flight.json()
    # check.equal(flight['origin'], flight_data['origin'], "Origin iata code mismatch")
    # check.equal(flight['destination'], flight_data['destination'], "Destination iata code mismatch")
    # check.equal(flight['departure_time'], flight_data['departure_time'], "Departure time mismatch")
    # check.equal(flight['arrival_time'], flight_data['arrival_time'], "Arrival time mismatch")
    # check.equal(flight['base_price'], flight_data['base_price'], "Base price mismatch")
    # check.equal(flight['aircraft_id'], flight_data['aircraft_id'], "Aircraft id mismatch")

    flight_double_creation = api_request(method="POST", path=FLIGHTS, json=flight_data, headers=auth_headers)
    assert flight_double_creation.status_code in (409, 422), f"Expected 409 or 422, got {flight_double_creation.status_code}"


@pytest.mark.parametrize('airport_data_1, airport_data_2, aircraft_data',[(good_airport_data_1, good_airport_data_2, good_aircraft_data)])
def test_update_flight(create_clear_flight, auth_headers):
    flight_data, flight_creation_json = create_clear_flight
    flight_id = flight_creation_json["id"]

    departure = fake.date_time(tzinfo=datetime.timezone.utc)
    arrival = departure + datetime.timedelta(hours=5)

    chagend_flight_data = {
        "origin": flight_data['destination'],
        "destination": flight_data['origin'],
        "departure_time": departure.isoformat().replace('+00:00', 'Z'),
        "arrival_time": arrival.isoformat().replace('+00:00', 'Z'),
        "base_price": 5000,
        "aircraft_id": flight_data['aircraft_id']
    }

    update_flight = api_request(method="PUT", path=f"{FLIGHTS}/{flight_id}", json=chagend_flight_data, headers=auth_headers)
    update_flight.raise_for_status()

    get_updated_flight = api_request(method="GET", path=f"{FLIGHTS}/{flight_id}", headers=auth_headers)
    updated_flight_json = get_updated_flight.json()
    check.equal(updated_flight_json['origin'], chagend_flight_data['origin'], "Origin iata code mismatch")
    check.equal(updated_flight_json['destination'], chagend_flight_data['destination'], "Destination iata code mismatch")
    check.equal(updated_flight_json['departure_time'], chagend_flight_data['departure_time'], "Departure time mismatch")
    check.equal(updated_flight_json['arrival_time'], chagend_flight_data['arrival_time'], "Arrival time mismatch")
    check.equal(updated_flight_json['base_price'], chagend_flight_data['base_price'], "Base price mismatch")
    check.equal(updated_flight_json['aircraft_id'], chagend_flight_data['aircraft_id'], "Aircraft id mismatch")


@pytest.mark.parametrize('airport_data_1, airport_data_2, aircraft_data',[(good_airport_data_1, good_airport_data_2, good_aircraft_data)])
@pytest.mark.order(35)
def test_get_all_flights(create_clear_flight, get_all_flights, auth_headers):
    validate(instance=get_all_flights, schema=flight_schema_array)


def test_flight_deleted_data_origin(flight_variable_path_teardown, auth_headers):
    api_request(method="DELETE", path=f"{AIRPORTS}/{good_airport_data_1['iata_code']}", headers=auth_headers, json=good_airport_data_1)
    origin = good_airport_data_1['iata_code']

    api_request(method="DELETE", path=f"{AIRPORTS}/{good_airport_data_2['iata_code']}", headers=auth_headers, json=good_airport_data_2)
    api_request(method="POST", path=AIRPORTS, headers=auth_headers, json=good_airport_data_2)
    destination = good_airport_data_2['iata_code']

    flight_variable_path_teardown.append({"path": f"{AIRPORTS}/{destination}"})

    aircraft = api_request(method="POST", path=AIRCRAFTS, headers=auth_headers, json=good_aircraft_data)
    aircraft_json = aircraft.json()
    aircraft_id = aircraft_json["id"]

    flight_variable_path_teardown.append({"path": f"{AIRCRAFTS}/{aircraft_id}"})

    departure = fake.date_time(tzinfo=datetime.timezone.utc)
    arrival = departure + datetime.timedelta(hours=5)

    flight_data = {
        "origin": origin,
        "destination": destination,
        "departure_time": departure.isoformat().replace('+00:00', 'Z'),
        "arrival_time": arrival.isoformat().replace('+00:00', 'Z'),
        "base_price": round(fake.pyfloat(left_digits=3, right_digits=2, positive=True), 2),
        "aircraft_id": aircraft_id
    }

    flight_creation = api_request(method="POST", path=FLIGHTS, json=flight_data, headers=auth_headers)
    flight_creation_json = flight_creation.json()
    flight_id = flight_creation_json["id"]
    flight_variable_path_teardown.append({"path": f"{FLIGHTS}/{flight_id}"})

    assert flight_creation.status_code == 422, f"Expected 422, got {flight_creation.status_code}, which means the flight was created despite using an origin which is not on the database"



def test_flight_deleted_data_destination(flight_variable_path_teardown, auth_headers):
    api_request(method="DELETE", path=f"{AIRPORTS}/{good_airport_data_1['iata_code']}", headers=auth_headers, json=good_airport_data_1)
    api_request(method="POST", path=AIRPORTS, headers=auth_headers, json=good_airport_data_1)
    origin = good_airport_data_1['iata_code']

    flight_variable_path_teardown.append({"path": f"{AIRPORTS}/{origin}"})

    api_request(method="DELETE", path=f"{AIRPORTS}/{good_airport_data_2['iata_code']}", headers=auth_headers, json=good_airport_data_2)
    destination = good_airport_data_2['iata_code']

    aircraft = api_request(method="POST", path=AIRCRAFTS, headers=auth_headers, json=good_aircraft_data)
    aircraft_json = aircraft.json()
    aircraft_id = aircraft_json["id"]

    flight_variable_path_teardown.append({"path": f"{AIRCRAFTS}/{aircraft_id}"})

    departure = fake.date_time(tzinfo=datetime.timezone.utc)
    arrival = departure + datetime.timedelta(hours=5)

    flight_data = {
        "origin": origin,
        "destination": destination,
        "departure_time": departure.isoformat().replace('+00:00', 'Z'),
        "arrival_time": arrival.isoformat().replace('+00:00', 'Z'),
        "base_price": round(fake.pyfloat(left_digits=3, right_digits=2, positive=True), 2),
        "aircraft_id": aircraft_id
    }

    flight_creation = api_request(method="POST", path=FLIGHTS, json=flight_data, headers=auth_headers)
    flight_creation_json = flight_creation.json()
    flight_id = flight_creation_json["id"]
    flight_variable_path_teardown.append({"path": f"{FLIGHTS}/{flight_id}"})

    assert flight_creation.status_code == 422, f"Expected 422, got {flight_creation.status_code}, which means the flight was created despite using a destination which is not on the database"



def test_flight_deleted_data_aircraft(flight_variable_path_teardown, auth_headers):
    api_request(method="DELETE", path=f"{AIRPORTS}/{good_airport_data_1['iata_code']}", headers=auth_headers, json=good_airport_data_1)
    api_request(method="POST", path=AIRPORTS, headers=auth_headers, json=good_airport_data_1)
    origin = good_airport_data_1['iata_code']

    flight_variable_path_teardown.append({"path": f"{AIRPORTS}/{origin}"})

    api_request(method="DELETE", path=f"{AIRPORTS}/{good_airport_data_2['iata_code']}", headers=auth_headers, json=good_airport_data_2)
    api_request(method="POST", path=AIRPORTS, headers=auth_headers, json=good_airport_data_2)
    destination = good_airport_data_2['iata_code']

    flight_variable_path_teardown.append({"path": f"{AIRPORTS}/{destination}"})

    aircraft = api_request(method="POST", path=AIRCRAFTS, headers=auth_headers, json=good_aircraft_data)
    aircraft_json = aircraft.json()
    aircraft_id = aircraft_json["id"]
    api_request(method="DELETE", path=f"{AIRPORTS}/{aircraft_id}", headers=auth_headers, json=good_aircraft_data)

    departure = fake.date_time(tzinfo=datetime.timezone.utc)
    arrival = departure + datetime.timedelta(hours=5)

    flight_data = {
        "origin": origin,
        "destination": destination,
        "departure_time": departure.isoformat().replace('+00:00', 'Z'),
        "arrival_time": arrival.isoformat().replace('+00:00', 'Z'),
        "base_price": round(fake.pyfloat(left_digits=3, right_digits=2, positive=True), 2),
        "aircraft_id": aircraft_id
    }

    flight_creation = api_request(method="POST", path=FLIGHTS, json=flight_data, headers=auth_headers)
    flight_creation_json = flight_creation.json()
    flight_id = flight_creation_json["id"]
    flight_variable_path_teardown.append({"path": f"{FLIGHTS}/{flight_id}"})

    assert flight_creation.status_code == 422, f"Expected 422, got {flight_creation.status_code}, which means the flight was created despite using an aircraft which is not on the database"



def test_flight_same_origin_destination_data(flight_variable_path_teardown, auth_headers):
    api_request(method="DELETE", path=f"{AIRPORTS}/{good_airport_data_1['iata_code']}", headers=auth_headers, json=good_airport_data_1)
    api_request(method="POST", path=AIRPORTS, headers=auth_headers, json=good_airport_data_1)
    origin = good_airport_data_1['iata_code']

    flight_variable_path_teardown.append({"path": f"{AIRPORTS}/{origin}"})

    aircraft = api_request(method="POST", path=AIRCRAFTS, headers=auth_headers, json=good_aircraft_data)
    aircraft_json = aircraft.json()
    aircraft_id = aircraft_json["id"]

    flight_variable_path_teardown.append({"path": f"{AIRCRAFTS}/{aircraft_id}"})

    departure = fake.date_time(tzinfo=datetime.timezone.utc)
    arrival = departure + datetime.timedelta(hours=5)

    flight_data = {
        "origin": origin,
        "destination": origin,
        "departure_time": departure.isoformat().replace('+00:00', 'Z'),
        "arrival_time": arrival.isoformat().replace('+00:00', 'Z'),
        "base_price": round(fake.pyfloat(left_digits=3, right_digits=2, positive=True), 2),
        "aircraft_id": aircraft_id
    }

    flight_creation = api_request(method="POST", path=FLIGHTS, json=flight_data, headers=auth_headers)
    flight_creation_json = flight_creation.json()
    flight_id = flight_creation_json["id"]
    flight_variable_path_teardown.append({"path": f"{FLIGHTS}/{flight_id}"})

    assert flight_creation.status_code == 422, f"Expected 422, got {flight_creation.status_code}, which means the flight was created despite using same origin and destination data"


