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


# @pytest.mark.happy_path_flow
# @pytest.mark.parametrize('airport_data', [good_airport_data])
# @pytest.mark.order(1)
# def test_clear_airport_data_happy_path_flow_1(delete_airport, airport_data):
#     pass
#
# @pytest.mark.happy_path_flow
# @pytest.mark.parametrize('airport_data', [good_airport_data])
# @pytest.mark.order(2)
# def test_create_and_airport_schema_happy_path_flow(create_airport, airport_data):
#     validate(instance=create_airport.json(), schema=airport_schema)
#
# @pytest.mark.happy_path_flow
# @pytest.mark.parametrize('airport_data', [good_airport_data])
# @pytest.mark.order(3)
# def test_repeat_create_airport_happy_path_flow(create_airport, airport_data):
#     status_code = create_airport.status_code
#     assert create_airport.status_code == 400, f"Expected 400 but got {status_code}"
#
# @pytest.mark.happy_path_flow
# @pytest.mark.order(4)
# @pytest.mark.parametrize('airport_data_old, airport_data_new',[(good_airport_data, changed_airport_data)])
# def test_update_airport_happy_path_flow(airport_data_new, airport_data_old, auth_headers):
#     r = api_request(method="PUT", path=f"/airports/{airport_data_old["iata_code"]}", json=airport_data_new, headers=auth_headers)
#     update_airport_json = r.json()
#     validate(instance=update_airport_json, schema=airport_schema)
#     check.equal(update_airport_json['iata_code'], changed_airport_data['iata_code'], "IATA code mismatch")
#     check.equal(update_airport_json['city'], changed_airport_data['city'], "City mismatch")
#     check.equal(update_airport_json['country'], changed_airport_data['country'], "Country mismatch")
#
# @pytest.mark.happy_path_flow
# @pytest.mark.parametrize('airport_data', [changed_airport_data])
# @pytest.mark.order(5)
# def test_validate_updated_airport_happy_path_flow(get_airport, airport_data):
#     get_airport_json = get_airport.json()
#     check.equal(get_airport_json['iata_code'], airport_data['iata_code'], "IATA code mismatch")
#     check.equal(get_airport_json['city'], airport_data['city'], "City mismatch")
#     check.equal(get_airport_json['country'], airport_data['country'], "Country mismatch")
#
# @pytest.mark.happy_path_flow
# @pytest.mark.parametrize('airport_data', [changed_airport_data])
# @pytest.mark.order(6)
# def test_clear_airport_data_happy_path_flow_2(delete_airport, airport_data):
#     status_code = delete_airport.status_code
#     assert delete_airport.status_code == 204, f"Expected 204 but got {status_code}"
#
# @pytest.mark.happy_path_flow
# @pytest.mark.parametrize('airport_data', [changed_airport_data])
# @pytest.mark.order(7)
# def test_validate_deleted_airport_happy_path_flow(get_airport, airport_data):
#     status_code = get_airport.status_code
#     assert get_airport.status_code == 404, f"Expected 404 but got {status_code}"



# TEST QUE VALIDA QUE AL HACER UN UPDATE DE UN AIRPORT A OTRO YA EXISTENTE (IATA INCLUIDO) FALLE

#
# @pytest.mark.update_to_existent_iata_code_flow
# @pytest.mark.parametrize('airport_data', [good_airport_data])
# @pytest.mark.order(8)
# def test_clear_airport_update_to_existent_iata_code_1(delete_airport, airport_data):
#     pass
#
# @pytest.mark.update_to_existent_iata_code_flow
# @pytest.mark.parametrize('airport_data', [changed_airport_data_iata_code])
# @pytest.mark.order(9)
# def test_clear_airport_update_to_existent_iata_code_2(delete_airport, airport_data):
#     pass
#
# @pytest.mark.update_to_existent_iata_code_flow
# @pytest.mark.parametrize('airport_data', [good_airport_data])
# @pytest.mark.order(10)
# def test_get_airport_update_to_existent_iata_code_1(get_airport, airport_data):
#     status_code = get_airport.status_code
#     assert get_airport.status_code == 404, f"Expected 404 but got {status_code}, iata_code: {airport_data["iata_code"]}"
#
# @pytest.mark.update_to_existent_iata_code_flow
# @pytest.mark.parametrize('airport_data', [changed_airport_data_iata_code])
# @pytest.mark.order(11)
# def test_get_airport_update_to_existent_iata_code_2(get_airport, airport_data):
#     status_code = get_airport.status_code
#     assert get_airport.status_code == 404, f"Expected 404 but got {status_code}, iata_code: {airport_data["iata_code"]}"
#
# @pytest.mark.update_to_existent_iata_code_flow
# @pytest.mark.parametrize('airport_data', [good_airport_data])
# @pytest.mark.order(12)
# def test_create_airport_update_to_existent_iata_code_1(create_airport, airport_data):
#     status_code = create_airport.status_code
#     assert create_airport.status_code == 201, f"Expected 201 but got {status_code}"
#
# @pytest.mark.update_to_existent_iata_code_flow
# @pytest.mark.parametrize('airport_data', [changed_airport_data_iata_code])
# @pytest.mark.order(13)
# def test_create_airport_update_to_existent_iata_code_2(create_airport, airport_data):
#     status_code = create_airport.status_code
#     assert create_airport.status_code == 201, f"Expected 201 but got {status_code}"
#
# @pytest.mark.update_to_existent_iata_code_flow
# @pytest.mark.parametrize('airport_data', [good_airport_data])
# @pytest.mark.order(14)
# def test_get_airport_update_to_existent_iata_code_3(get_airport, airport_data):
#     status_code = get_airport.status_code
#     assert get_airport.status_code == 200, f"Expected 200 but got {status_code}, iata_code: {airport_data["iata_code"]}"
#
# @pytest.mark.update_to_existent_iata_code_flow
# @pytest.mark.parametrize('airport_data', [changed_airport_data_iata_code])
# @pytest.mark.order(15)
# def test_get_airport_update_to_existent_iata_code_4(get_airport, airport_data):
#     status_code = get_airport.status_code
#     assert get_airport.status_code == 200, f"Expected 200 but got {status_code}, iata_code: {airport_data["iata_code"]}"
#
# @pytest.mark.update_to_existent_iata_code_flow
# @pytest.mark.order(16)
# @pytest.mark.parametrize('airport_data_old, airport_data_new',[(good_airport_data, changed_airport_data_iata_code)])
# def test_update_airport_update_to_existent_iata_code(airport_data_new, airport_data_old, auth_headers):
#     r = api_request(method="PUT", path=f"/airports/{airport_data_old["iata_code"]}", json=airport_data_new, headers=auth_headers)
#     assert r.status_code == 404, f"Expected 404 but got {r.status_code}"
# # BUG - DOESN'T FAIL AND CHANGES DATA FROM OLD TO NEW, BUT DOESN'T CHANGE PATH
#
# @pytest.mark.update_to_existent_iata_code_flow
# @pytest.mark.parametrize('airport_data', [changed_airport_data_iata_code])
# @pytest.mark.order(17)
# def test_validate_airport_update_to_existent_iata_code_1(get_airport, airport_data):
#     get_airport_json = get_airport.json()
#     check.equal(get_airport_json['iata_code'], changed_airport_data_iata_code['iata_code'], "IATA code mismatch")
#     check.equal(get_airport_json['city'], changed_airport_data_iata_code['city'], "City mismatch")
#     check.equal(get_airport_json['country'], changed_airport_data_iata_code['country'], "Country mismatch")
#
# @pytest.mark.update_to_existent_iata_code_flow
# @pytest.mark.parametrize('airport_data', [good_airport_data])
# @pytest.mark.order(18)
# def test_validate_airport_update_to_existent_iata_code_2(get_airport, airport_data):
#     get_airport_json = get_airport.json()
#     check.equal(get_airport_json['iata_code'], good_airport_data['iata_code'], "IATA code mismatch")
#     check.equal(get_airport_json['city'], good_airport_data['city'], "City mismatch")
#     check.equal(get_airport_json['country'], good_airport_data['country'], "Country mismatch")
# # BUG - FAIL - CHENGED WHEN IT SHOULDNT HAVE
#
# @pytest.mark.update_to_existent_iata_code_flow
# @pytest.mark.parametrize('airport_data', [good_airport_data])
# @pytest.mark.order(19)
# def test_clear_airport_update_to_existent_iata_code_3(delete_airport, airport_data):
#     status_code = delete_airport.status_code
#     assert delete_airport.status_code == 204, f"Expected 204 but got {status_code}"
#
# @pytest.mark.update_to_existent_iata_code_flow
# @pytest.mark.parametrize('airport_data', [changed_airport_data_iata_code])
# @pytest.mark.order(20)
# def test_clear_airport_update_to_existent_iata_code_4(delete_airport, airport_data):
#     status_code = delete_airport.status_code
#     assert delete_airport.status_code == 204, f"Expected 204 but got {status_code}"
#
# @pytest.mark.update_to_existent_iata_code_flow
# @pytest.mark.parametrize('airport_data', [good_airport_data])
# @pytest.mark.order(21)
# def test_validate_deleted_airport_update_to_existent_iata_code_1(get_airport, airport_data):
#     status_code = get_airport.status_code
#     assert get_airport.status_code == 404, f"Expected 404 but got {status_code}"
#
# @pytest.mark.update_to_existent_iata_code_flow
# @pytest.mark.parametrize('airport_data', [changed_airport_data_iata_code])
# @pytest.mark.order(22)
# def test_validate_deleted_airport_update_to_existent_iata_code_2(get_airport, airport_data):
#     status_code = get_airport.status_code
#     assert get_airport.status_code == 404, f"Expected 404 but got {status_code}"


# TEST QUE VALIDA QUE AL HACER UPDATE DE UN AIRPORT A OTRO NO EXISTENTE, EFECTUE LOS CAMBIOS Y VER QUE PASA CON HACER UN CAMBIO EN EL IATA CODE
# SPOILER ALERT: CAMBIA EL IATA CODE, PERO NO CAMBIA EL PATH DE LA URL, CONTINUA CON EL VIEJO

# @pytest.mark.update_iata_code_flow
# @pytest.mark.parametrize('airport_data', [good_airport_data])
# @pytest.mark.order(23)
# def test_clear_airport_update_iata_code_1(delete_airport, airport_data):
#     pass
#
# @pytest.mark.update_iata_code_flow
# @pytest.mark.order(24)
# @pytest.mark.parametrize('airport_data', [good_airport_data])
# def test_create_airport_update_iata_code(create_airport, airport_data):
#     status_code = create_airport.status_code
#     assert create_airport.status_code == 201, f"Expected 201 but got {status_code}"
#
# @pytest.mark.update_iata_code_flow
# @pytest.mark.parametrize('airport_data', [changed_airport_data_iata_code])
# @pytest.mark.order(25)
# def test_clear_airport_update_iata_code_2(delete_airport, airport_data):
#     pass
#
# @pytest.mark.update_iata_code_flow
# @pytest.mark.parametrize('airport_data_old, airport_data_new',[(good_airport_data, changed_airport_data_iata_code)])
# @pytest.mark.order(26)
# def test_update_airport_update_iata_code(airport_data_old, airport_data_new, auth_headers):
#     r = api_request(method="PUT", path=f"/airports/{airport_data_old["iata_code"]}", json=airport_data_new, headers=auth_headers)
#     update_airport_json = r.json()
#     validate(instance=update_airport_json, schema=airport_schema)
#     check.equal(update_airport_json['iata_code'], changed_airport_data_iata_code['iata_code'], "IATA code mismatch")
#     check.equal(update_airport_json['city'], changed_airport_data_iata_code['city'], "City mismatch")
#     check.equal(update_airport_json['country'], changed_airport_data_iata_code['country'], "Country mismatch")
# SHOULD FAIL AND NOT LET IATA_CODE CHANGE, OR IT COULD CHANGE, BUT ALSO CHANGE URL PATH
# DOESNT FAIL - BUG
#
# @pytest.mark.update_iata_code_flow
# @pytest.mark.parametrize('airport_data', [changed_airport_data_iata_code])
# @pytest.mark.order(27)
# def test_validate_new_airport_update_iata_code(get_airport, airport_data):
#     status_code = get_airport.status_code
#     assert get_airport.status_code == 200, f"Expected 200 but got {status_code}, iata_code: {airport_data["iata_code"]}"
# # FAIL - BUG - iata_code changes in the json but it doesn't change on the URL path, it countinues to be the original one
#
# @pytest.mark.update_iata_code_flow
# @pytest.mark.parametrize('airport_data', [good_airport_data])
# @pytest.mark.order(28)
# def test_validate_old_airport_update_iata_code(get_airport, airport_data):
#     status_code = get_airport.status_code
#     assert get_airport.status_code == 404, f"Expected 404 but got {status_code}, iata_code: {airport_data["iata_code"]}"
# # FAIL - BUG - iata_code changes in the json but it doesn't change on the URL path, it countinues to be the original one
#
# @pytest.mark.update_iata_code_flow
# @pytest.mark.parametrize('airport_data', [good_airport_data])
# @pytest.mark.order(29)
# def test_clear_airport_update_iata_code_3(delete_airport, airport_data):
#     status_code = delete_airport.status_code
#     assert delete_airport.status_code == 204, f"Expected 204 but got {status_code}"
#
# @pytest.mark.update_iata_code_flow
# @pytest.mark.parametrize('airport_data', [changed_airport_data_iata_code])
# @pytest.mark.order(30)
# def test_clear_airport_update_iata_code_4(delete_airport, airport_data):
#     status_code = delete_airport.status_code
#     assert delete_airport.status_code == 204, f"Expected 204 but got {status_code}"
#

# NEGATIVE TESTS
#
# @pytest.mark.negative_flow
# @pytest.mark.parametrize('airport_data', bad_airport_data)
# @pytest.mark.order(32)
# def test_clear_airport_negative_flow_1(delete_airport, airport_data):
#     pass
#
# @pytest.mark.negative_flow
# @pytest.mark.parametrize('airport_data', bad_airport_data)
# @pytest.mark.order(33)
# def test_create_airport_fail_negative_flow(create_airport, airport_data):
#     status_code = create_airport.status_code
#     assert status_code == 422, f"Expected 422 but got {status_code} for input: {airport_data}"
#
# @pytest.mark.negative_flow
# @pytest.mark.parametrize('airport_data', bad_airport_data)
# @pytest.mark.order(34)
# def test_clear_airport_negative_flow_2(delete_airport, airport_data):
#     pass



@pytest.mark.get_all_airports
@pytest.mark.order(35)
def test_get_all_airports(get_all_airports):
    validate(instance=get_all_airports, schema=airport_schema_array)



@pytest.mark.parametrize('airport_data_1', [good_airport_data_1])
def test_create_clear_airport_new_1(create_clear_airport_1, airport_data_1):
    validate(instance=create_clear_airport_1, schema=airport_schema)



@pytest.mark.negative_flow
@pytest.mark.parametrize('airport_data', bad_airport_data)
def test_create_clear_airport_fail_negative_flow(create_clear_airport_negative_test, airport_data, auth_headers):
    r = create_clear_airport_negative_test
    status_code = r.status_code

    assert status_code in (400, 422), f"Expected 400 or 422, got {status_code}: {r.text}"

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


@pytest.mark.parametrize('airport_data_1', [good_airport_data])
def test_double_create_airport(create_clear_airport_1, airport_data_1, auth_headers):
    repeat_create_airport = api_request(method="POST", path=AIRPORTS, headers=auth_headers, json=airport_data_1)
    assert repeat_create_airport.status_code in (400, 422), f"Expected 400 but got {repeat_create_airport.status_code}"


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


@pytest.mark.parametrize('airport_data_1, airport_data_2',[(good_airport_data, changed_airport_data_iata_code)])
def test_update_to_existing_iata_code(create_clear_airport_1, create_clear_airport_2, airport_data_1, airport_data_2, auth_headers):
    airport_created_1 = create_clear_airport_1
    airport_created_1_iata_code = airport_created_1["iata_code"]

    airport_created_2 = create_clear_airport_2
    airport_created_2_iata_code = airport_created_2["iata_code"]

    update = api_request(method="PUT", path=f"{AIRPORTS}/{airport_created_1_iata_code}", json=airport_data_2, headers=auth_headers)
    assert update.status_code == 422, f"Airport was updated to an already existing iata_code {airport_created_2_iata_code} when it shouldn't have."


