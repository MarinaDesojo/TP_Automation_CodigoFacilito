import pytest, requests, os
from jsonschema import validate, ValidationError
from test_schema import user_schema
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS
from API_project.utils.fixture_utils import admin_token, auth_headers


def test_create_user_schema(user):
    validate(instance=user, schema=user_schema)


def test_get_all_users(user, auth_headers, limit=50):
    skip = 0
    results = []

    while True:
        r = requests.get(f"{BASE_URL}{USERS}", headers=auth_headers, params={"skip": skip, "limit": limit}, timeout=5)
        r.raise_for_status()
        users_list = r.json()

        if not users_list:
            break
        results.extend(users_list)
        skip += limit
    return results


def test_get_user(user, auth_headers):
    r = requests.get(f"{BASE_URL}{USERS}/me", headers=auth_headers, timeout=5)
    assert r.status_code == 200
