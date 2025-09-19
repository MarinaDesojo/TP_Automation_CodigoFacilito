import time

import pytest, requests
from API_project.utils.api_helpers import api_request
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS, USERS_ME
from API_project.tests.users.test_schema import user_schema, changed_user_data, good_user_data, bad_user_data, user_schema_array
from API_project.utils.fixture_utils import admin_token, auth_headers

# @pytest.fixture
# def create_user(auth_headers, user_data):
#     r = api_request(method="POST", path=USERS, json=user_data, headers=auth_headers)
#     r.raise_for_status()  # da error en caso de que no devuelva 200
#     return r.json()
#
# @pytest.fixture
# def user_id(create_user):
#     return create_user["id"]


# @pytest.fixture
# def get_all_users(auth_headers):
#     r = api_request(method="GET", path=USERS, headers=auth_headers)
#     return r

@pytest.fixture
def get_all_users(auth_headers, limit=50):
    skip = 0
    results = []
    while True:
        r = api_request(method="GET", path=USERS, headers=auth_headers, params={"skip": skip, "limit": limit})
        r.raise_for_status()
        users_list = r.json()
        if not users_list:
            break
        results.extend(users_list)
        skip += limit
    return results

@pytest.fixture
def get_user(auth_headers, user_data):
    r = api_request(method="GET", path=USERS_ME, headers=auth_headers)
    return r

@pytest.fixture
def update_user(auth_headers, user_data):
    r = api_request(method="PUT", path=f'{USERS}/{user_data["user_id"]}', json=user_data, headers=auth_headers)
    return r

@pytest.fixture
def delete_user(auth_headers, user_id):
    r = api_request(method="DELETE", path=f'{USERS}/{user_id}', headers=auth_headers)
    return r


@pytest.fixture
def create_clear_user(user_data, auth_headers):
    r = api_request(method="POST", path=USERS, json=user_data, headers=auth_headers)
    r.raise_for_status()
    user_created = r.json()
    yield user_created
    api_request(method="DELETE", path=f"{USERS}/{user_created['id']}", headers=auth_headers)


# @pytest.fixture
# def create_clear_user_negative_test(user_data, auth_headers):
#     r = api_request(method="POST", path=USERS, json=user_data, headers=auth_headers)
#     yield r
#     try:
#         if r.status_code < 400:
#             user_created = r.json()
#             user_id = user_created.get('id')
#             if user_id:
#                 retries = 3
#                 for attempt in range(retries):
#                     d = api_request(method="DELETE", path=f"{USERS}/{user_id}", headers=auth_headers)
#                     if d.status_code == 204:
#                         break
#                     else:
#                         time.sleep(1)
#                 else:
#                     print(f"Warning: Failed to delete user {user_id} after {retries} attempts")
#             else:
#                 print("Warning: User creation response missing 'id', skipping delete")
#     except Exception as e:
#         print(f"Exception during cleanup: {e}")



@pytest.fixture
def create_clear_user_negative_test(user_data, auth_headers):
    r = api_request(method="POST", path=USERS, json=user_data, headers=auth_headers)
    yield r
    try:
        user_created = r.json()
        user_id = user_created.get('id')
        if user_id:
            retries = 3
            for attempt in range(retries):
                d = api_request(method="DELETE", path=f"{USERS}/{user_id}", headers=auth_headers)
                if d.status_code == 204:
                    break
                else:
                    time.sleep(1)
            else:
                print(f"Warning: Failed to delete user {user_id} after {retries} attempts")
        else:
            print("Warning: User creation response missing 'id', skipping delete")
    except Exception as e:
        print(f"Exception during cleanup: {e}")