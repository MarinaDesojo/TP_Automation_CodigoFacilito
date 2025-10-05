import pytest
from jsonschema import validate
import pytest_check as check
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS, USERS_ME
from API_project.tests.users.test_schema import user_schema, changed_user_data, good_user_data, bad_user_data, user_schema_array
from API_project.utils.fixture_utils import auth_headers
from API_project.utils.api_helpers import api_request

@pytest.mark.happy_path_flow
@pytest.mark.parametrize('user_data', [good_user_data])
@pytest.mark.order(1)
def test_create_delete_user_schema(create_clear_user, user_data):
    validate(instance=create_clear_user, schema=user_schema)

@pytest.mark.parametrize('user_data', [good_user_data])
@pytest.mark.order(2)
def test_double_create(create_clear_user, user_data, auth_headers):
    r = api_request(method="POST", path=USERS, data=user_data, headers=auth_headers)
    assert r.status_code in[400, 409, 422], f"Expected 400, 409 or 422, but got {r.status_code}: {r.text}"


@pytest.mark.parametrize('user_data, user_data_new',[(good_user_data, changed_user_data)])
@pytest.mark.order(3)
def test_update_user_values(create_clear_user, user_data, user_data_new, auth_headers):
    user_created_json = create_clear_user
    r = api_request(method="PUT", path=f'{USERS}/{user_created_json["id"]}', json=user_data_new, headers=auth_headers)
    r.raise_for_status()
    r_get = api_request(method="GET", path=USERS, headers=auth_headers)
    users = r_get.json()
    target_email = user_data_new["email"]
    target_full_name = user_data_new["full_name"]
    target_role = user_data_new["role"]
    found_email = any(
        isinstance(user, dict) and user.get("email") == target_email
        for user in users)
    check.is_true(found_email, f"User with updated email not found: {target_email}")
    # assert found, f"User with updated data not found: {user_data_new['email']}"
    found_full_name = any(
        isinstance(user, dict) and user.get("full_name") == target_full_name
        for user in users)
    check.is_true(found_full_name, f"User with updated full_name not found: {target_full_name}")
    # assert found, f"User with updated data not found: {user_data_new['full_name']}"
    found_role = any(
        isinstance(user, dict) and user.get("role") == target_role
        for user in users)
    check.is_true(found_role, f"User with updated role not found: {target_role}")
    # assert found, f"User with updated data not found: {user_data_new['role']}"



# @pytest.mark.negative_flow
# @pytest.mark.parametrize('user_data', bad_user_data)
# def test_create_clear_user_fail_negative_flow(create_clear_user_negative_test, user_data):
#     status_code = create_clear_user_negative_test.status_code
#     assert status_code == 422, f"Expected 422 but got {status_code} for input: {user_data}"

#cambiar a mover a test? para poder hacer un get y delete de los email que cree yo?

@pytest.mark.order(4)
@pytest.mark.negative_flow
@pytest.mark.parametrize('user_data', bad_user_data)
def test_create_clear_user_fail_negative_flow(create_clear_user_negative_test, user_data, auth_headers):
    r = create_clear_user_negative_test
    status_code = r.status_code

    assert status_code in (400, 422), f"Expected 400 or 422, got {status_code}: {r.text}"

    email = user_data.get('email')
    if email:
        get_resp = api_request(method="GET", path=USERS, headers=auth_headers, params={"email": email})
        users_found = get_resp.json()
        for user in users_found:
            if user.get('email') == email:
                print(f"Warning, user was created despite of {status_code} for: {email}")
                # borrar usuario encontrado (por si quedó colgado)
                delete_resp = api_request(method="DELETE", path=f"{USERS}/{user['id']}", headers=auth_headers)
                if delete_resp.status_code != 204:
                    print(f"Warning: Failed to delete user {user['id']} with email {email}")




# @pytest.mark.happy_path_flow
# @pytest.mark.parametrize('user_data', [good_user_data])
# @pytest.mark.order(2)
# def test_clear_user_data_happy_path_flow_1(delete_user, user_id):
#     assert delete_user.status_code == 204







@pytest.mark.order(5)
@pytest.mark.parametrize('user_data', [good_user_data])
def test_get_user_me(get_user):
    assert get_user.status_code == 200

@pytest.mark.order(6)
def test_get_all_users_schema(get_all_users):
    validate(instance=get_all_users, schema=user_schema_array)

#assert any(user['email'] == 'test@example.com' for user in data)

