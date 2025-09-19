import pytest
from jsonschema import validate
import pytest_check as check
from API_project.tests.airports.test_schema import bad_airport_data, changed_airport_data, changed_airport_data_iata_code, airport_schema_array, good_airport_data, airport_schema
from API_project.utils.fixture_utils import auth_headers
from API_project.utils.api_helpers import api_request

@pytest.mark.happy_path_flow
@pytest.mark.parametrize('airport_data', [good_airport_data])
@pytest.mark.order(1)
def test_clear_airport_data_happy_path_flow_1(delete_airport, airport_data):
    pass

@pytest.mark.happy_path_flow
@pytest.mark.parametrize('airport_data', [good_airport_data])
@pytest.mark.order(2)
def test_create_and_airport_schema_happy_path_flow(create_airport, airport_data):
    validate(instance=create_airport.json(), schema=airport_schema)

@pytest.mark.happy_path_flow
@pytest.mark.parametrize('airport_data', [good_airport_data])
@pytest.mark.order(3)
def test_repeat_create_airport_happy_path_flow(create_airport, airport_data):
    status_code = create_airport.status_code
    assert create_airport.status_code == 400, f"Expected 400 but got {status_code}"

@pytest.mark.happy_path_flow
@pytest.mark.order(4)
@pytest.mark.parametrize('airport_data_old, airport_data_new',[(good_airport_data, changed_airport_data)])
def test_update_airport_happy_path_flow(airport_data_new, airport_data_old, auth_headers):
    r = api_request(method="PUT", path=f"/airports/{airport_data_old["iata_code"]}", json=airport_data_new, headers=auth_headers)
    update_airport_json = r.json()
    validate(instance=update_airport_json, schema=airport_schema)
    check.equal(update_airport_json['iata_code'], changed_airport_data['iata_code'], "IATA code mismatch")
    check.equal(update_airport_json['city'], changed_airport_data['city'], "City mismatch")
    check.equal(update_airport_json['country'], changed_airport_data['country'], "Country mismatch")

@pytest.mark.happy_path_flow
@pytest.mark.parametrize('airport_data', [changed_airport_data])
@pytest.mark.order(5)
def test_validate_updated_airport_happy_path_flow(get_airport, airport_data):
    get_airport_json = get_airport.json()
    check.equal(get_airport_json['iata_code'], airport_data['iata_code'], "IATA code mismatch")
    check.equal(get_airport_json['city'], airport_data['city'], "City mismatch")
    check.equal(get_airport_json['country'], airport_data['country'], "Country mismatch")

@pytest.mark.happy_path_flow
@pytest.mark.parametrize('airport_data', [changed_airport_data])
@pytest.mark.order(6)
def test_clear_airport_data_happy_path_flow_2(delete_airport, airport_data):
    status_code = delete_airport.status_code
    assert delete_airport.status_code == 204, f"Expected 204 but got {status_code}"

@pytest.mark.happy_path_flow
@pytest.mark.parametrize('airport_data', [changed_airport_data])
@pytest.mark.order(7)
def test_validate_deleted_airport_happy_path_flow(get_airport, airport_data):
    status_code = get_airport.status_code
    assert get_airport.status_code == 404, f"Expected 404 but got {status_code}"



# TEST QUE VALIDA QUE AL HACER UN UPDATE DE UN AIRPORT A OTRO YA EXISTENTE (IATA INCLUIDO) FALLE


@pytest.mark.update_to_existent_iata_code_flow
@pytest.mark.parametrize('airport_data', [good_airport_data])
@pytest.mark.order(8)
def test_clear_airport_update_to_existent_iata_code_1(delete_airport, airport_data):
    pass

@pytest.mark.update_to_existent_iata_code_flow
@pytest.mark.parametrize('airport_data', [changed_airport_data_iata_code])
@pytest.mark.order(9)
def test_clear_airport_update_to_existent_iata_code_2(delete_airport, airport_data):
    pass

@pytest.mark.update_to_existent_iata_code_flow
@pytest.mark.parametrize('airport_data', [good_airport_data])
@pytest.mark.order(10)
def test_get_airport_update_to_existent_iata_code_1(get_airport, airport_data):
    status_code = get_airport.status_code
    assert get_airport.status_code == 404, f"Expected 404 but got {status_code}, iata_code: {airport_data["iata_code"]}"

@pytest.mark.update_to_existent_iata_code_flow
@pytest.mark.parametrize('airport_data', [changed_airport_data_iata_code])
@pytest.mark.order(11)
def test_get_airport_update_to_existent_iata_code_2(get_airport, airport_data):
    status_code = get_airport.status_code
    assert get_airport.status_code == 404, f"Expected 404 but got {status_code}, iata_code: {airport_data["iata_code"]}"

@pytest.mark.update_to_existent_iata_code_flow
@pytest.mark.parametrize('airport_data', [good_airport_data])
@pytest.mark.order(12)
def test_create_airport_update_to_existent_iata_code_1(create_airport, airport_data):
    status_code = create_airport.status_code
    assert create_airport.status_code == 201, f"Expected 201 but got {status_code}"

@pytest.mark.update_to_existent_iata_code_flow
@pytest.mark.parametrize('airport_data', [changed_airport_data_iata_code])
@pytest.mark.order(13)
def test_create_airport_update_to_existent_iata_code_2(create_airport, airport_data):
    status_code = create_airport.status_code
    assert create_airport.status_code == 201, f"Expected 201 but got {status_code}"

@pytest.mark.update_to_existent_iata_code_flow
@pytest.mark.parametrize('airport_data', [good_airport_data])
@pytest.mark.order(14)
def test_get_airport_update_to_existent_iata_code_3(get_airport, airport_data):
    status_code = get_airport.status_code
    assert get_airport.status_code == 200, f"Expected 200 but got {status_code}, iata_code: {airport_data["iata_code"]}"

@pytest.mark.update_to_existent_iata_code_flow
@pytest.mark.parametrize('airport_data', [changed_airport_data_iata_code])
@pytest.mark.order(15)
def test_get_airport_update_to_existent_iata_code_4(get_airport, airport_data):
    status_code = get_airport.status_code
    assert get_airport.status_code == 200, f"Expected 200 but got {status_code}, iata_code: {airport_data["iata_code"]}"

@pytest.mark.update_to_existent_iata_code_flow
@pytest.mark.order(16)
@pytest.mark.parametrize('airport_data_old, airport_data_new',[(good_airport_data, changed_airport_data_iata_code)])
def test_update_airport_update_to_existent_iata_code(airport_data_new, airport_data_old, auth_headers):
    r = api_request(method="PUT", path=f"/airports/{airport_data_old["iata_code"]}", json=airport_data_new, headers=auth_headers)
    assert r.status_code == 404, f"Expected 404 but got {r.status_code}"
# BUG - DOESN'T FAIL AND CHANGES DATA FROM OLD TO NEW, BUT DOESN'T CHANGE PATH

@pytest.mark.update_to_existent_iata_code_flow
@pytest.mark.parametrize('airport_data', [changed_airport_data_iata_code])
@pytest.mark.order(17)
def test_validate_airport_update_to_existent_iata_code_1(get_airport, airport_data):
    get_airport_json = get_airport.json()
    check.equal(get_airport_json['iata_code'], changed_airport_data_iata_code['iata_code'], "IATA code mismatch")
    check.equal(get_airport_json['city'], changed_airport_data_iata_code['city'], "City mismatch")
    check.equal(get_airport_json['country'], changed_airport_data_iata_code['country'], "Country mismatch")

@pytest.mark.update_to_existent_iata_code_flow
@pytest.mark.parametrize('airport_data', [good_airport_data])
@pytest.mark.order(18)
def test_validate_airport_update_to_existent_iata_code_2(get_airport, airport_data):
    get_airport_json = get_airport.json()
    check.equal(get_airport_json['iata_code'], good_airport_data['iata_code'], "IATA code mismatch")
    check.equal(get_airport_json['city'], good_airport_data['city'], "City mismatch")
    check.equal(get_airport_json['country'], good_airport_data['country'], "Country mismatch")
# BUG - FAIL - CHENGED WHEN IT SHOULDNT HAVE

@pytest.mark.update_to_existent_iata_code_flow
@pytest.mark.parametrize('airport_data', [good_airport_data])
@pytest.mark.order(19)
def test_clear_airport_update_to_existent_iata_code_3(delete_airport, airport_data):
    status_code = delete_airport.status_code
    assert delete_airport.status_code == 204, f"Expected 204 but got {status_code}"

@pytest.mark.update_to_existent_iata_code_flow
@pytest.mark.parametrize('airport_data', [changed_airport_data_iata_code])
@pytest.mark.order(20)
def test_clear_airport_update_to_existent_iata_code_4(delete_airport, airport_data):
    status_code = delete_airport.status_code
    assert delete_airport.status_code == 204, f"Expected 204 but got {status_code}"

@pytest.mark.update_to_existent_iata_code_flow
@pytest.mark.parametrize('airport_data', [good_airport_data])
@pytest.mark.order(21)
def test_validate_deleted_airport_update_to_existent_iata_code_1(get_airport, airport_data):
    status_code = get_airport.status_code
    assert get_airport.status_code == 404, f"Expected 404 but got {status_code}"

@pytest.mark.update_to_existent_iata_code_flow
@pytest.mark.parametrize('airport_data', [changed_airport_data_iata_code])
@pytest.mark.order(22)
def test_validate_deleted_airport_update_to_existent_iata_code_2(get_airport, airport_data):
    status_code = get_airport.status_code
    assert get_airport.status_code == 404, f"Expected 404 but got {status_code}"


# TEST QUE VALIDA QUE AL HACER UPDATE DE UN AIRPORT A OTRO NO EXISTENTE, EFECTUE LOS CAMBIOS Y VER QUE PASA CON HACER UN CAMBIO EN EL IATA CODE
# SPOILER ALERT: CAMBIA EL IATA CODE, PERO NO CAMBIA EL PATH DE LA URL, CONTINUA CON EL VIEJO

@pytest.mark.update_iata_code_flow
@pytest.mark.parametrize('airport_data', [good_airport_data])
@pytest.mark.order(23)
def test_clear_airport_update_iata_code_1(delete_airport, airport_data):
    pass

@pytest.mark.update_iata_code_flow
@pytest.mark.order(24)
@pytest.mark.parametrize('airport_data', [good_airport_data])
def test_create_airport_update_iata_code(create_airport, airport_data):
    status_code = create_airport.status_code
    assert create_airport.status_code == 201, f"Expected 201 but got {status_code}"

@pytest.mark.update_iata_code_flow
@pytest.mark.parametrize('airport_data', [changed_airport_data_iata_code])
@pytest.mark.order(25)
def test_clear_airport_update_iata_code_2(delete_airport, airport_data):
    pass

@pytest.mark.update_iata_code_flow
@pytest.mark.parametrize('airport_data_old, airport_data_new',[(good_airport_data, changed_airport_data_iata_code)])
@pytest.mark.order(26)
def test_update_airport_update_iata_code(airport_data_old, airport_data_new, auth_headers):
    r = api_request(method="PUT", path=f"/airports/{airport_data_old["iata_code"]}", json=airport_data_new, headers=auth_headers)
    update_airport_json = r.json()
    validate(instance=update_airport_json, schema=airport_schema)
    check.equal(update_airport_json['iata_code'], changed_airport_data_iata_code['iata_code'], "IATA code mismatch")
    check.equal(update_airport_json['city'], changed_airport_data_iata_code['city'], "City mismatch")
    check.equal(update_airport_json['country'], changed_airport_data_iata_code['country'], "Country mismatch")
# SHOULD FAIL AND NOT LET IATA_CODE CHANGE, OR IT COULD CHANGE, BUT ALSO CHANGE URL PATH
# DOESNT FAIL - BUG

@pytest.mark.update_iata_code_flow
@pytest.mark.parametrize('airport_data', [changed_airport_data_iata_code])
@pytest.mark.order(27)
def test_validate_new_airport_update_iata_code(get_airport, airport_data):
    status_code = get_airport.status_code
    assert get_airport.status_code == 200, f"Expected 200 but got {status_code}, iata_code: {airport_data["iata_code"]}"
# FAIL - BUG - iata_code changes in the json but it doesn't change on the URL path, it countinues to be the original one

@pytest.mark.update_iata_code_flow
@pytest.mark.parametrize('airport_data', [good_airport_data])
@pytest.mark.order(28)
def test_validate_old_airport_update_iata_code(get_airport, airport_data):
    status_code = get_airport.status_code
    assert get_airport.status_code == 404, f"Expected 404 but got {status_code}, iata_code: {airport_data["iata_code"]}"
# FAIL - BUG - iata_code changes in the json but it doesn't change on the URL path, it countinues to be the original one

@pytest.mark.update_iata_code_flow
@pytest.mark.parametrize('airport_data', [good_airport_data])
@pytest.mark.order(29)
def test_clear_airport_update_iata_code_3(delete_airport, airport_data):
    status_code = delete_airport.status_code
    assert delete_airport.status_code == 204, f"Expected 204 but got {status_code}"

@pytest.mark.update_iata_code_flow
@pytest.mark.parametrize('airport_data', [changed_airport_data_iata_code])
@pytest.mark.order(30)
def test_clear_airport_update_iata_code_4(delete_airport, airport_data):
    status_code = delete_airport.status_code
    assert delete_airport.status_code == 204, f"Expected 204 but got {status_code}"


# DOUBLE DELETE TEST

@pytest.mark.double_delete
@pytest.mark.parametrize('airport_data', [good_airport_data])
@pytest.mark.order(31)
def test_clear_airport_2asd(delete_airport, airport_data):
    status_code = delete_airport.status_code
    assert delete_airport.status_code == 404, f"Expected 404 but got {status_code}"
# FAILS - BUG, GET 204 DESPITE OF PATH (IATA_CODE) NOT CREATED



# NEGATIVE TESTS

@pytest.mark.negative_flow
@pytest.mark.parametrize('airport_data', bad_airport_data)
@pytest.mark.order(32)
def test_clear_airport_negative_flow_1(delete_airport, airport_data):
    pass

@pytest.mark.negative_flow
@pytest.mark.parametrize('airport_data', bad_airport_data)
@pytest.mark.order(33)
def test_create_airport_fail_negative_flow(create_airport, airport_data):
    status_code = create_airport.status_code
    assert status_code == 422, f"Expected 422 but got {status_code} for input: {airport_data}"

@pytest.mark.negative_flow
@pytest.mark.parametrize('airport_data', bad_airport_data)
@pytest.mark.order(34)
def test_clear_airport_negative_flow_2(delete_airport, airport_data):
    pass



@pytest.mark.get_all_airports
@pytest.mark.order(35)
def test_get_all_airports(get_all_airports):
    validate(instance=get_all_airports, schema=airport_schema_array)
