import pytest, requests, os
from jsonschema import validate, ValidationError
from test_schema import airport_schema, fixed_airport_data, random_airport_data
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS
from API_project.utils.api_helpers import api_request

def test_create_airport_schema(airport):
    validate(instance=airport, schema=airport_schema)


def test_get_all_airports(airport, auth_headers):
    r = requests.get(f"{BASE_URL}{AIRPORTS}", headers=auth_headers)
    assert r.status_code == 200 #si quiero ver lo que hay en lista tengo que poner el breakpoing en esta linea, frena antes de ejecutar la linea donde se colocar
    assert r.text != "" #esto verifica que el texto dentro del response no se encuentre vecio, ver en debug


def test_get_airport(auth_headers):
    r = api_request(method="POST", url=f"{BASE_URL}{AIRPORTS}", headers=auth_headers, data=fixed_airport_data)
    create_airport_response = r.json()  # crea una variable con el json de la response
    api_request()
    requests.put(f'{BASE_URL}{AIRPORTS}/{create_airport_response["iata_code"]}', headers=auth_headers, timeout=5)


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


