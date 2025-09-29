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

# @pytest.mark.parametrize('airport_data_1, airport_data_2, aircraft_data',[(good_airport_data_1, good_airport_data_2, good_aircraft_data)])
# def test_create_clear_flight(create_clear_airport_1, create_clear_airport_2, create_clear_aircraft, auth_headers):
#     origin = create_clear_airport_1.get("iata_code")
#     destination = create_clear_airport_2.get("iata_code")
#     aircraft_id = create_clear_aircraft.get("id")
#
#     departure = fake.date_time(tzinfo=datetime.timezone.utc)
#     arrival = departure + datetime.timedelta(hours=5)
#
#     flight_data = {
#         "origin": origin,
#         "destination": destination,
#         "departure_time": departure.isoformat().replace('+00:00', 'Z'),
#         "arrival_time": arrival.isoformat().replace('+00:00', 'Z'),
#         "base_price": round(fake.pyfloat(left_digits=3, right_digits=2, positive=True), 2),
#         "aircraft_id": aircraft_id
#     }
#
#     flight_creation = api_request(method="POST", path=FLIGHTS, json=flight_data, headers=auth_headers)
#     validate(instance=flight_creation.json(), schema=flight_schema)
#     flight_creation_id = flight_creation.json()["id"]
#
#     get_flight = api_request(method="GET", path=f"{FLIGHTS}/{flight_creation_id}", headers=auth_headers)
#     flight = get_flight.json()
#     check.equal(flight['origin'], flight_data['origin'], "Origin iata code mismatch")
#     check.equal(flight['destination'], flight_data['destination'], "Destination iata code mismatch")
#     check.equal(flight['departure_time'], flight_data['departure_time'], "Departure time mismatch")
#     check.equal(flight['arrival_time'], flight_data['arrival_time'], "Arrival time mismatch")
#     check.equal(flight['base_price'], flight_data['base_price'], "Base price mismatch")
#     check.equal(flight['aircraft_id'], flight_data['aircraft_id'], "Aircraft id mismatch")
#
#     MAX_RETRIES = 3
#
#     for attempt in range(1, MAX_RETRIES + 1):
#         try:
#             api_request(method="DELETE", path=f"{FLIGHTS}/{flight_creation_id}", headers=auth_headers)
#             get_flight_after_delete = api_request(method="GET", path=f"{FLIGHTS}/{flight_creation_id}", headers=auth_headers)
#             if get_flight_after_delete.status_code in (404, 422):
#                 print("Flight deleted successfully")
#                 break
#             else:
#                 print (f"Flight still exists, status {get_flight_after_delete.status_code}, retrying delete")
#         except Exception as e:
#             print (f"Error during request {e}")
#     else:
#         raise Exception(f"Flight was not deleted after {MAX_RETRIES} attempts")


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





# doble post mismo flight_data
# update y ver si se updateo bien
# update a otro ya creado?
# get all flights validate schema


