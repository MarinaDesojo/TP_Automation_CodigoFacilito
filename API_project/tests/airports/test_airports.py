import pytest, requests, os
from jsonschema import validate, ValidationError

from API_project.tests.airports.conftest import delete_airport
from API_project.tests.airports.test_schema import bad_airport_data, changed_airport_data
from API_project.utils.fixture_utils import auth_headers
from test_schema import airport_schema, good_airport_data, random_airport_data
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS
from API_project.utils.api_helpers import api_request

@pytest.mark.parametrize('airport_data', [good_airport_data])
@pytest.mark.order(1)
def test_clear_airport(delete_airport, airport_data):
    pass

@pytest.mark.parametrize('airport_data', [good_airport_data])
@pytest.mark.order(2)
def test_airport_schema(create_airport, airport_data):
    validate(instance=create_airport.json(), schema=airport_schema)

@pytest.mark.parametrize('airport_data', bad_airport_data)
@pytest.mark.order(3)
def test_create_airport_fail(create_airport, airport_data):
    assert create_airport.status_code ==  422

# @pytest.mark.parametrize(['iata_code', 'airport_data'], [(good_airport_data["iata_code"]), (changed_airport_data)])
@pytest.mark.parametrize('airport_data', [changed_airport_data])
@pytest.mark.order(4)
def test_update_airport(update_airport, airport_data):
    update_airport_json = update_airport.json()
    validate(instance=update_airport_json, schema=airport_schema)
    assert update_airport_json['iata_code'] == airport_data['iata_code']
    assert update_airport_json['city'] == airport_data['city']
    assert update_airport_json['country'] == airport_data['country']

@pytest.mark.parametrize('airport_data', [changed_airport_data])
@pytest.mark.order(5)
def test_validate_updated_airport(get_airport, airport_data):
    get_airport_json = get_airport.json()
    assert get_airport_json['iata_code'] == airport_data['iata_code']
    assert get_airport_json['city'] == airport_data['city']
    assert get_airport_json['country'] == airport_data['country']

@pytest.mark.parametrize('airport_data', [changed_airport_data])
@pytest.mark.order(6)
def test_clear_airport_updated(delete_airport, airport_data):
    assert delete_airport.status_code == 204

@pytest.mark.parametrize('airport_data', [changed_airport_data])
@pytest.mark.order(7)
def test_validate_deleted_airport(get_airport, airport_data):
    assert get_airport.status_code == 404



# def test_get_all_airports_old(airport, auth_headers, airport_data):
#     r = requests.get(f"{BASE_URL}{AIRPORTS}", headers=auth_headers)
#     assert r.status_code == 200 #si quiero ver lo que hay en lista tengo que poner el breakpoing en esta linea, frena antes de ejecutar la linea donde se colocar
#     assert r.text != "" #esto verifica que el texto dentro del response no se encuentre vecio, ver en debug
#
# def test_get_all_airports(get_all_airports):
#     r = get_all_airports()
#
# def test_get_airport(auth_headers):
#     r = api_request(method="POST", url=f"{BASE_URL}{AIRPORTS}", headers=auth_headers, data=good_airport_data)
#     create_airport_response = r.json()  # crea una variable con el json de la response
#     api_request()
#     requests.put(f'{BASE_URL}{AIRPORTS}/{create_airport_response["iata_code"]}', headers=auth_headers, timeout=5)


# def test_create_update_get_delete_airport(airport, auth_headers):
#     airport_creation = {
#         "iata_code": "RTU",
#         "city": "La Paz",
#         "country": fake.country_code()  # faker para datos random mokeados
#     }
#     airport()
#     assert r.status_code == 200
#
#
#     airport_modification = {
#         "iata_code": "{airport_response['iata_code']}",
#         "city": "La Paz",
#         "country": fake.country_code()  # faker para datos random mokeados
#     }
#     r = requests.get(f"{BASE_URL}{AIRPORT}/{fixed_iata_code}", headers=auth_headers, data=airport_schema, timeout=5)
#
#     requests.put(f"{BASE_URL}{AIRPORT}/{airport_response["iata_code"]}", json=airport_modification, headers=auth_headers, timeout=5)
#
#     r = requests.get(f"{BASE_URL}{AIRPORT}/{fixed_iata_code}", headers=auth_headers, data=airport_schema, timeout=5)


