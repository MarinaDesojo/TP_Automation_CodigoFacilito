import pytest
import pytest_check as check
import time
from jsonschema import validate

from API_project.tests.airports.test_schema import bad_airport_data, changed_airport_data, \
    changed_airport_data_iata_code, airport_schema_array, good_airport_data, airport_schema, good_airport_data_1, \
    good_airport_data_2
from API_project.utils.api_helpers import api_request
from API_project.utils.fixture_utils import auth_headers
from API_project.utils.settings import AIRPORTS

@pytest.mark.api
@pytest.mark.happy_path_flow
@pytest.mark.parametrize('airport_data_1', [good_airport_data_1])
def test_create_clear_airport_new_1(create_clear_airport_1, airport_data_1):
    validate(instance=create_clear_airport_1, schema=airport_schema)

@pytest.mark.api
@pytest.mark.get_all_airports
def test_get_all_airports(get_all_airports):
    validate(instance=get_all_airports, schema=airport_schema_array)

@pytest.mark.api
@pytest.mark.parametrize('airport_data_1, airport_data_2',[(good_airport_data, changed_airport_data)])
def test_update_airport_data_not_iata_code(create_clear_airport_1, airport_data_1, airport_data_2, auth_headers):
    airport_created = create_clear_airport_1
    airport_created_iata_code = airport_created.get('iata_code')

    update_airport_2 = api_request(method="PUT", path=f"{AIRPORTS}/{airport_created_iata_code}", json=airport_data_2, headers=auth_headers)
    update_airport_2.raise_for_status()
    update_airport_2_json = update_airport_2.json()

    get_airport_1 = api_request(method="GET", path=f"{AIRPORTS}/{airport_created_iata_code}", headers=auth_headers)
    get_airport_1_json = get_airport_1.json()
    check.equal(update_airport_2_json['iata_code'], get_airport_1_json['iata_code'], "IATA code mismatch")
    check.equal(update_airport_2_json['city'], get_airport_1_json['city'], "City mismatch")
    check.equal(update_airport_2_json['country'], get_airport_1_json['country'], "Country mismatch")


@pytest.mark.api
@pytest.mark.fail
@pytest.mark.parametrize('airport_data_1, airport_data_2',[(good_airport_data, changed_airport_data_iata_code)])
def test_update_to_existing_iata_code(create_clear_airport_1, create_clear_airport_2, airport_data_1, airport_data_2, auth_headers):
    airport_created_1 = create_clear_airport_1
    airport_created_1_iata_code = airport_created_1["iata_code"]

    airport_created_2 = create_clear_airport_2
    airport_created_2_iata_code = airport_created_2["iata_code"]

    update = api_request(method="PUT", path=f"{AIRPORTS}/{airport_created_1_iata_code}", json=airport_data_2, headers=auth_headers)
    assert update.status_code == 422, f"Expected 422, got {update.status_code}. This suggests the API accepted updating the airport data to an already existing iata_code {airport_created_2_iata_code} when it shouldn't have, or failed to return the correct validation error."

@pytest.mark.api
@pytest.mark.parametrize('airport_data_1, airport_data_2',[(good_airport_data, changed_airport_data_iata_code)])
def test_update_iata_code_airport(create_clear_airport_1, airport_data_1, airport_data_2, auth_headers):
    airport_created = create_clear_airport_1
    airport_created_iata_code = airport_created.get('iata_code')

    MAX_RETRIES = 5
    airport_to_update_iata_code = airport_data_2["iata_code"]
    for attempt in range(MAX_RETRIES):
        get_airport = api_request(method="GET", path=f'{AIRPORTS}/{airport_to_update_iata_code}', headers=auth_headers)

        if get_airport.status_code == 404:
            print(f"[Attempt {attempt + 1}] Airport {airport_to_update_iata_code} not found. Safe to update to this airport data.")
            break

        print(f"[Attempt {attempt + 1}] Airport still exists (status: {get_airport.status_code}), trying DELETE...")
        delete_airport = api_request(method="DELETE", path=f'{AIRPORTS}/{airport_to_update_iata_code}', headers=auth_headers)
        print(f"[Attempt {attempt + 1}] DELETE returned status {delete_airport.status_code}")

        time.sleep(1)
    else:
        raise Exception(f"Failed to delete airport {airport_to_update_iata_code} after {MAX_RETRIES} attempts")

    update_airport_2 = api_request(method="PUT", path=f"{AIRPORTS}/{airport_created_iata_code}", json=airport_data_2, headers=auth_headers)
    update_airport_2_json = update_airport_2.json()
    update_airport_2_iata_code = update_airport_2_json['iata_code']
    if update_airport_2.status_code in (404, 422):
        print(f"Airport iata_code data was not allowed to change from {airport_created_iata_code} to {update_airport_2_iata_code}")
    else:
        print(f"Airport iata_code data was allowed to change from {airport_created_iata_code} to {update_airport_2_iata_code}")

    get_airport_1 = api_request(method="GET", path=f"{AIRPORTS}/{airport_created_iata_code}", headers=auth_headers)
    if get_airport_1.status_code != 404:
        print(f"Airport iata_code {airport_created_iata_code} path still exists when should've changed if update was successful.")
        get_airport_1_json = get_airport_1.json()
        check.equal(airport_created['iata_code'], get_airport_1_json['iata_code'], "IATA code mismatch")
        check.equal(airport_created['city'], get_airport_1_json['city'], "City mismatch")
        check.equal(airport_created['country'], get_airport_1_json['country'], "Country mismatch")
    else:
        pass

    get_airport_2 = api_request(method="GET", path=f"{AIRPORTS}/{update_airport_2_iata_code}", headers=auth_headers)
    if get_airport_2.status_code in (200, 204):
        print(f"Airport iata_code was updated on the path too")
        get_airport_2_json = get_airport_2.json()
        check.equal(update_airport_2_json['iata_code'], get_airport_2_json['iata_code'], "IATA code mismatch")
        check.equal(update_airport_2_json['city'], get_airport_2_json['city'], "City mismatch")
        check.equal(update_airport_2_json['country'], get_airport_2_json['country'], "Country mismatch")
    else:
        print(f"Airport iata_code {update_airport_2_iata_code} not found, path was not updated despite updating the iata_code.")

    if api_request(method="GET", path=f"{AIRPORTS}/{update_airport_2_iata_code}", headers=auth_headers).status_code not in [400, 422]:
        api_request(method="DELETE", path=f"{AIRPORTS}/{update_airport_2_iata_code}", headers=auth_headers)

@pytest.mark.api
@pytest.mark.fail
@pytest.mark.parametrize('airport_data_1', [good_airport_data])
def test_double_create_airport(create_clear_airport_1, airport_data_1, auth_headers):
    repeat_create_airport = api_request(method="POST", path=AIRPORTS, headers=auth_headers, json=airport_data_1)
    assert repeat_create_airport.status_code in (400, 422), f"Expected 400 but got {repeat_create_airport.status_code}. This suggests the API accepted creating an airport with the same ariport data than an already existing airport, or failed to return the correct validation error."

@pytest.mark.api
@pytest.mark.fail
@pytest.mark.parametrize('airport_data', bad_airport_data)
def test_create_clear_airport_fail_negative_flow(create_clear_airport_negative_test, airport_data, auth_headers):
    r = create_clear_airport_negative_test
    status_code = r.status_code

    assert status_code in (400, 422), f"Expected 400 or 422, got {status_code} for {airport_data}. This suggests the API accepted airport data with non valid or missing data, or failed to return the correct validation error."

    iata_code = airport_data.get('iata_code')
    if iata_code:
        get_resp = api_request(method="GET", path=AIRPORTS, headers=auth_headers, params={"iata_code": iata_code})
        airports_found = get_resp.json()
        for airport in airports_found:
            if airport.get('iata_code') == iata_code:
                print(f"Warning, airport was created despite of {status_code} for: {iata_code}")

                delete_resp = api_request(method="DELETE", path=f"{AIRPORTS}/{airport['iata_code']}", headers=auth_headers)
                if delete_resp.status_code != 204:
                    print(f"Warning: Failed to delete airport {iata_code}")

@pytest.mark.api
@pytest.mark.fail
@pytest.mark.parametrize('airport_data_1', [good_airport_data_1])
def test_create_clear_airport_not_authenticated(create_clear_airport_fail_not_authenticated):
    airport_created_status_code = create_clear_airport_fail_not_authenticated
    assert airport_created_status_code in (401, 403), f"Expected 401 or 403, got {airport_created_status_code}. This suggests the API accepted an airport creation request without authentication, or failed to return the correct validation error."

