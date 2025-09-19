import pytest
from API_project.utils.api_helpers import api_request
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS, USERS_ME
from API_project.utils.fixture_utils import admin_token, auth_headers

@pytest.fixture
def create_airport(auth_headers, airport_data):
    r = api_request(method="POST", path=AIRPORTS, json=airport_data, headers=auth_headers)
    return r

@pytest.fixture
def get_all_airports(auth_headers, limit=50):
    skip = 0
    results = []
    while True:
        r = api_request(method="GET", path=AIRPORTS, headers=auth_headers, params={"skip": skip, "limit": limit})
        r.raise_for_status()
        airports_list = r.json()
        if not airports_list:
            break
        results.extend(airports_list)
        skip += limit
    return results


@pytest.fixture
def get_airport(auth_headers, airport_data):
    r = api_request(method="GET", path=f'{AIRPORTS}/{airport_data["iata_code"]}', headers=auth_headers)
    return r

@pytest.fixture
def update_airport(auth_headers, airport_data):
    r = api_request(method="PUT", path=f'{AIRPORTS}/{airport_data["iata_code"]}', json=airport_data, headers=auth_headers)
    return r

@pytest.fixture
def delete_airport(auth_headers, airport_data):
    r = api_request(method="DELETE", path=f'{AIRPORTS}/{airport_data["iata_code"]}', headers=auth_headers)
    return r

