import pytest
from jsonschema import validate
import pytest_check as check
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS, USERS_ME
from API_project.tests.aircrafts.test_schema import bad_aircraft_data, changed_aircraft_data, aircraft_schema_array, good_aircraft_data, aircraft_schema, random_aircraft_data
from API_project.utils.fixture_utils import auth_headers
from API_project.utils.api_helpers import api_request

@pytest.mark.happy_path_flow
@pytest.mark.parametrize('aircraft_data', [good_aircraft_data])
@pytest.mark.order(1)
def test_create_delete_aircraft_schema(create_clear_aircraft, aircraft_data):
    validate(instance=create_clear_aircraft, schema=aircraft_schema)

@pytest.mark.parametrize('aircraft_data', [good_aircraft_data])
@pytest.mark.order(2)
def test_double_create(create_clear_aircraft, aircraft_data, auth_headers):
    r = api_request(method="POST", path=AIRCRAFTS, data=aircraft_data, headers=auth_headers)
    assert r.status_code in[400, 409, 422], f"Expected 400, 409 or 422, but got {r.status_code}: {r.text}"


@pytest.mark.parametrize('aircraft_data, aircraft_data_new',[(good_aircraft_data, changed_aircraft_data)])
@pytest.mark.order(3)
def test_update_aircraft_values(create_clear_aircraft, aircraft_data, aircraft_data_new, auth_headers):
    aircraft_created = create_clear_aircraft
    r = api_request(method="PUT", path=f'{AIRCRAFTS}/{aircraft_created["id"]}', json=aircraft_data_new, headers=auth_headers)
    assert r.status_code == 200, f"Expected 200, but got {r.status_code}"
    r_get = api_request(method="GET", path=f'{AIRCRAFTS}/{aircraft_created["id"]}', headers=auth_headers)
    update_aircraft_json = r_get.json()
    check.equal(update_aircraft_json['tail_number'], changed_aircraft_data['tail_number'], "Tail number mismatch")
    check.equal(update_aircraft_json['model'], changed_aircraft_data['model'], "Model mismatch")
    check.equal(update_aircraft_json['capacity'], changed_aircraft_data['capacity'], "Capacity mismatch")

@pytest.mark.order(4)
@pytest.mark.negative_flow
@pytest.mark.parametrize('aircraft_data', bad_aircraft_data)
def test_create_clear_aircraft_fail_negative_flow(create_clear_aircraft_negative_test, aircraft_data, auth_headers):
    r = create_clear_aircraft_negative_test
    status_code = r.status_code

    assert status_code in (400, 422), f"Expected 400 or 422, got {status_code}: {r.text}"

    try:
        aircraft_id = r.json().get("id")
    except Exception:
        aircraft_id = None

    if aircraft_id:
        get_resp = api_request(method="GET", path=f"{AIRCRAFTS}/{aircraft_id}", headers=auth_headers)
        if get_resp.status_code in (200, 204):
            print(f"Warning, aircraft was created despite receiving status {status_code} for: {aircraft_data}")
            delete_resp = api_request(method="DELETE", path=f"{AIRCRAFTS}/{aircraft_id}", headers=auth_headers)
            if delete_resp.status_code != 204:
                print(f"Warning: Failed to delete aircraft {aircraft_id}")


@pytest.mark.order(5)
def test_get_all_aircrafts(get_all_aircrafts):
    validate(instance=get_all_aircrafts, schema=aircraft_schema_array)







