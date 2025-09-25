import pytest, datetime
from jsonschema import validate
import pytest_check as check

from API_project.tests.airports.test_schema import good_airport_data
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS, USERS_ME
from API_project.tests.aircrafts.test_schema import bad_aircraft_data, changed_aircraft_data, aircraft_schema_array, good_aircraft_data, aircraft_schema
from API_project.utils.fixture_utils import auth_headers
from API_project.utils.api_helpers import api_request
from API_project.tests.airports.conftest import create_clear_airport
from API_project.tests.airports.test_schema import good_airport_data, changed_airport_data_iata_code
from API_project.tests.flights.test_schema import flight_schema, flight_schema_array, good_flight_data, changed_flight_data, bad_flight_data, random_flight_data


#
# @pytest.mark.happy_path_flow
# @pytest.mark.parametrize('aircraft_data', [good_aircraft_data])
# @pytest.mark.order(1)
# def test_create_delete_aircraft_schema(create_clear_aircraft, aircraft_data):
#     validate(instance=create_clear_aircraft, schema=aircraft_schema)
#
# @pytest.mark.parametrize('aircraft_data', [good_aircraft_data])
# @pytest.mark.order(2)
# def test_double_create(create_clear_aircraft, aircraft_data, auth_headers):
#     r = api_request(method="POST", path=AIRCRAFTS, data=aircraft_data, headers=auth_headers)
#     assert r.status_code in[400, 409, 422], f"Expected 400, 409 or 422, but got {r.status_code}: {r.text}"
#
#
# @pytest.mark.parametrize('aircraft_data, aircraft_data_new',[(good_aircraft_data, changed_aircraft_data)])
# @pytest.mark.order(3)
# def test_update_aircraft_values(create_clear_aircraft, aircraft_data, aircraft_data_new, auth_headers):
#     aircraft_created = create_clear_aircraft
#     r = api_request(method="PUT", path=f'{AIRCRAFTS}/{aircraft_created["id"]}', json=aircraft_data_new, headers=auth_headers)
#     assert r.status_code == 200, f"Expected 200, but got {r.status_code}"
#     r_get = api_request(method="GET", path=f'{AIRCRAFTS}/{aircraft_created["id"]}', headers=auth_headers)
#     update_aircraft_json = r_get.json()
#     check.equal(update_aircraft_json['tail_number'], changed_aircraft_data['tail_number'], "Tail number mismatch")
#     check.equal(update_aircraft_json['model'], changed_aircraft_data['model'], "Model mismatch")
#     check.equal(update_aircraft_json['capacity'], changed_aircraft_data['capacity'], "Capacity mismatch")
#
# @pytest.mark.order(4)
# @pytest.mark.negative_flow
# @pytest.mark.parametrize('aircraft_data', bad_aircraft_data)
# def test_create_clear_aircraft_fail_negative_flow(create_clear_aircraft_negative_test, aircraft_data, auth_headers):
#     r = create_clear_aircraft_negative_test
#     status_code = r.status_code
#
#     assert status_code in (400, 422), f"Expected 400 or 422, got {status_code}: {r.text}"
#
#     try:
#         aircraft_id = r.json().get("id")
#     except Exception:
#         aircraft_id = None
#
#     if aircraft_id:
#         get_resp = api_request(method="GET", path=f"{AIRCRAFTS}/{aircraft_id}", headers=auth_headers)
#         if get_resp.status_code in (200, 204):
#             print(f"Warning, aircraft was created despite receiving status {status_code} for: {aircraft_data}")
#             delete_resp = api_request(method="DELETE", path=f"{AIRCRAFTS}/{aircraft_id}", headers=auth_headers)
#             if delete_resp.status_code != 204:
#                 print(f"Warning: Failed to delete aircraft {aircraft_id}")
#
#
# @pytest.mark.order(5)
# def test_get_all_aircrafts(get_all_aircrafts):
#     validate(instance=get_all_aircrafts, schema=aircraft_schema_array)
#
#
#
#





def test_create_clear_flight(auth_headers):
    airport1 = api_request(method="POST", path=AIRPORTS, json=good_airport_data, headers=auth_headers)
    airport1.raise_for_status()
    airport1_json = airport1.json()
    origin = airport1_json.get("iata_code")

    airport2 = api_request(method="POST", path=AIRPORTS, json=changed_airport_data_iata_code, headers=auth_headers)
    airport2.raise_for_status()
    airport2_json = airport2.json()
    destination = airport2_json.get("iata_code")

    aircraft = api_request(method="POST", path=AIRCRAFTS, json=good_aircraft_data, headers=auth_headers)
    aircraft.raise_for_status()
    aircraft_json = aircraft.json()
    aircraft_id = aircraft_json.get("id")

    departure = fake.date_time(tzinfo=datetime.timezone.utc)
    arrival = departure + datetime.timedelta(hours=5)

    flight_data = {
        "origin": origin,
        "destination": destination,
        "departure_time": departure.isoformat(timespec='milliseconds').replace('+00:00', 'Z'),
        "arrival_time": arrival.isoformat(timespec='milliseconds').replace('+00:00', 'Z'),
        "base_price": round(fake.pyfloat(left_digits=3, right_digits=2, positive=True), 2),
        "aircraft_id": aircraft_id
    }

    flight_creation = api_request(method="POST", path=FLIGHTS, json=flight_data, headers=auth_headers)
    validate(instance=flight_creation.json(), schema=flight_schema)
    flight_creation_id = flight_creation.json()["id"]
    get_flight = api_request(method="GET", path=f"FLIGHTS/{flight_creation_id}", headers=auth_headers)
    flight = get_flight.json()
    check.equal(flight['origin'], flight_data['origin'], "Origin iata code mismatch")
    check.equal(flight['destination'], flight_data['destination'], "Destination iata code mismatch")
    check.equal(flight['departure_time'], flight_data['departure_time'], "Departure time mismatch")
    check.equal(flight['arrival_time'], flight_data['arrival_time'], "Arrival time mismatch")
    check.equal(flight['base_price'], flight_data['base_price'], "Base price mismatch")
    check.equal(flight['aircraft_id'], flight_data['aircraft_id'], "Aircraft id mismatch")

    api_request(method="DELETE", path=f"AIRPORTS/{origin}", headers=auth_headers)
    api_request(method="DELETE", path=f"AIRPORTS/{destination}", headers=auth_headers)
    api_request(method="DELETE", path=f"AIRCRAFTS/{aircraft_id}", headers=auth_headers)
    api_request(method="DELETE", path=f"FLIGHTS/{flight_creation_id}", headers=auth_headers)
