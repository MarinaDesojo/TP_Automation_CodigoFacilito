import pytest, time
from API_project.utils.api_helpers import api_request
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS, USERS_ME
from API_project.utils.fixture_utils import admin_token, auth_headers

# @pytest.fixture
# def create_aircraft(auth_headers, aircraft_data):
#     r = api_request(method="POST", path=AIRCRAFTS, json=aircraft_data, headers=auth_headers)
#     return r
#
# @pytest.fixture
# def get_all_aircrafts(auth_headers, limit=50):
#     skip = 0
#     results = []
#     while True:
#         r = api_request(method="GET", path=AIRCRAFTS, headers=auth_headers, params={"skip": skip, "limit": limit})
#         r.raise_for_status()
#         aircrafts_list = r.json()
#         if not aircrafts_list:
#             break
#         results.extend(aircrafts_list)
#         skip += limit
#     return results
#
#
# @pytest.fixture
# def get_aircraft(auth_headers, aircraft_data):
#     r = api_request(method="GET", path=f'{AIRCRAFTS}/{aircraft_data["iata_code"]}', headers=auth_headers)
#     return r
#
# @pytest.fixture
# def update_aircraft(auth_headers, aircraft_data):
#     r = api_request(method="PUT", path=f'{AIRCRAFTS}/{aircraft_data["iata_code"]}', json=aircraft_data, headers=auth_headers)
#     return r
#
# @pytest.fixture
# def delete_aircraft(auth_headers, aircraft_data):
#     r = api_request(method="DELETE", path=f'{AIRCRAFTS}/{aircraft_data["iata_code"]}', headers=auth_headers)
#     return r
#
#
#




@pytest.fixture
def get_all_aircrafts(auth_headers, limit=50):
    skip = 0
    results = []
    while True:
        r = api_request(method="GET", path=AIRCRAFTS, headers=auth_headers, params={"skip": skip, "limit": limit})
        r.raise_for_status()
        aircrafts_list = r.json()
        if not aircrafts_list:
            break
        results.extend(aircrafts_list)
        skip += limit
    return results

@pytest.fixture
def get_aircraft(auth_headers, aircraft_data):
    r = api_request(method="GET", path=AIRCRAFTS, headers=auth_headers)
    return r

@pytest.fixture
def update_aircraft(auth_headers, aircraft_data, aircraft_data_new):
    r = api_request(method="PUT", path=f'{AIRCRAFTS}/{aircraft_data["id"]}', json=aircraft_data_new, headers=auth_headers)
    return r

@pytest.fixture
def delete_aircraft(auth_headers, aircraft_id):
    r = api_request(method="DELETE", path=f'{AIRCRAFTS}/{aircraft_id}', headers=auth_headers)
    return r

@pytest.fixture
def create_clear_aircraft(aircraft_data, auth_headers):
    r = api_request(method="POST", path=AIRCRAFTS, json=aircraft_data, headers=auth_headers)
    r.raise_for_status()
    aircraft_created = r.json()
    yield aircraft_created
    try:
        aircraft_created = r.json()
        aircraft_id = aircraft_created.get('id')
        if aircraft_id:
            retries = 3
            for attempt in range(retries):
                d = api_request(method="DELETE", path=f"{AIRCRAFTS}/{aircraft_id}", headers=auth_headers)
                if d.status_code == 204:
                    break
                else:
                    time.sleep(1)
            else:
                print(f"Warning: Failed to delete user {aircraft_id} after {retries} attempts")
        else:
            print("Warning: User creation response missing 'id', skipping delete")
    except Exception as e:
        print(f"Exception during cleanup: {e}")

@pytest.fixture
def create_clear_aircraft_negative_test(aircraft_data, auth_headers):
    r = api_request(method="POST", path=USERS, json=aircraft_data, headers=auth_headers)
    yield r
    try:
        aircraft_created = r.json()
        aircraft_id = aircraft_created.get('id')
        if aircraft_id:
            retries = 3
            for attempt in range(retries):
                d = api_request(method="DELETE", path=f"{AIRCRAFTS}/{aircraft_id}", headers=auth_headers)
                if d.status_code == 204:
                    break
                else:
                    time.sleep(1)
            else:
                print(f"Warning: Failed to delete user {aircraft_id} after {retries} attempts")
        else:
            print("Warning: Aircraft creation response missing 'id', skipping delete")
    except Exception as e:
        print(f"Exception during cleanup: {e}")