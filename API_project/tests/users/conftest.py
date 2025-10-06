import time

import pytest, requests
from API_project.utils.api_helpers import api_request
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS, USERS_ME
from API_project.tests.users.test_schema import user_schema, changed_user_data, good_user_data, bad_user_data, user_schema_array
from API_project.utils.fixture_utils import admin_token, auth_headers

@pytest.fixture
def create_clear_user(user_data, auth_headers):
    MAX_RETRIES = 5
    target_email = user_data["email"]

    for attempt in range(1, MAX_RETRIES + 1):
        get_users = api_request(method="GET", path=USERS, headers=auth_headers)

        if get_users.status_code != 200:
            print(f"[Attempt {attempt}] Failed to fetch users, status: {get_users.status_code}")
            time.sleep(1)
            continue

        users = get_users.json()
        target_user = next((user for user in users if user["email"] == target_email), None)

        if not target_user:
            print(f"[Attempt {attempt}] User with email {target_email} not found. Safe to create.")
            break

        user_id = target_user["id"]
        print(f"[Attempt {attempt}] User found (ID: {user_id}), attempting DELETE...")

        delete_user = api_request(method="DELETE", path=f"{USERS}/{user_id}", headers=auth_headers)
        print(f"[Attempt {attempt}] DELETE returned status {delete_user.status_code}")

        verify_user = api_request(method="GET", path=f"{USERS}/{user_id}", headers=auth_headers)
        if verify_user.status_code in (404, 422):
            print("User deleted successfully.")
            break
        elif verify_user.status_code == 405:
            print("GET by user ID not allowed — assuming user was deleted.")
            break
        else:
            print("User still exists, retrying...")
            time.sleep(1)
    else:
        raise Exception(f"Failed to delete user with email {target_email} after {MAX_RETRIES} attempts")

    user_created = api_request(method="POST", path=USERS, json=user_data, headers=auth_headers)
    user_created.raise_for_status()
    user_created_json = user_created.json()

    yield user_created_json
    try:
        user_id = user_created_json["id"]
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
def get_user(auth_headers):
    r = api_request(method="GET", path=USERS_ME, headers=auth_headers)
    return r

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


@pytest.fixture
def create_clear_user_fail_not_authenticated(user_data, auth_headers):
    MAX_RETRIES = 5
    target_email = user_data["email"]

    for attempt in range(1, MAX_RETRIES + 1):
        get_users = api_request(method="GET", path=USERS, headers=auth_headers)

        if get_users.status_code != 200:
            print(f"[Attempt {attempt}] Failed to fetch users, status: {get_users.status_code}")
            time.sleep(1)
            continue

        users = get_users.json()
        target_user = next((user for user in users if user["email"] == target_email), None)

        if not target_user:
            print(f"[Attempt {attempt}] User with email {target_email} not found. Safe to create.")
            break

        user_id = target_user["id"]
        print(f"[Attempt {attempt}] User found (ID: {user_id}), attempting DELETE...")

        delete_user = api_request(method="DELETE", path=f"{USERS}/{user_id}", headers=auth_headers)
        print(f"[Attempt {attempt}] DELETE returned status {delete_user.status_code}")

        verify_user = api_request(method="GET", path=f"{USERS}/{user_id}", headers=auth_headers)
        if verify_user.status_code in (404, 422):
            print("User deleted successfully.")
            break
        elif verify_user.status_code == 405:
            print("GET by user ID not allowed — assuming user was deleted.")
            break
        else:
            print("User still exists, retrying...")
            time.sleep(1)
    else:
        raise Exception(f"Failed to delete user with email {target_email} after {MAX_RETRIES} attempts")

    user_created = api_request(method="POST", path=USERS, json=user_data)
    user_created_status_code = user_created.status_code

    yield user_created_status_code
    try:
        user_id = user_created.json().get('id')
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