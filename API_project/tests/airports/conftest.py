# Aquí podés definir fixtures reutilizables, un conftest por cada directorio
import random
import string
import requests, pytest

from API_project.utils.api_helpers import api_request
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS
from API_project.utils.fixture_utils import admin_token, auth_headers
from test_schema import random_airport_data

# @pytest.fixture
# def airport(auth_headers):
#     airport_data = random_airport_data
#
#     r = requests.post(BASE_URL + AIRPORTS, json=airport_data, headers=auth_headers, timeout=5)
#     r.raise_for_status()
#     airport_response = r.json() #crea una variable con el json de la response
#     yield airport_response #para probar el airport_response en el mismo fixture
#
#     (requests.delete(f'{BASE_URL}{AIRPORTS}/{airport_response["iata_code"]}', headers=auth_headers, timeout=5))


@pytest.fixture
def create_airport(auth_headers, airport_data):
    r = api_request(method="POST", path=AIRPORTS, json=airport_data, headers=auth_headers)
    return r.json()

@pytest.fixture
def get_all_airports(auth_headers):
    r = api_request(method="GET", path=AIRPORTS, headers=auth_headers)
    return r.json()

@pytest.fixture
def get_airport(auth_headers, airport_data):
    r = api_request(method="GET", path=f'{AIRPORTS}/{airport_data["iata_code"]}', headers=auth_headers)
    return r.json()

@pytest.fixture
def update_airport(auth_headers, airport_data):
    r = api_request(method="PUT", path=f'{AIRPORTS}/{airport_data["iata_code"]}', headers=auth_headers)
    return r.json()

@pytest.fixture
def delete_airport(auth_headers, airport_data):
    r = api_request(method="DELETE", path=f'{AIRPORTS}/{airport_data["iata_code"]}', headers=auth_headers)
    return r.json()





#crear otros fixture con datos fijos para poder utilizar para otros test, y despues no olvidar de borrarlos

def test_airport(airport):
    print(airport)
