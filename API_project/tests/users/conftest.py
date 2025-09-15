# Aquí podés definir fixtures reutilizables, un conftest por cada directorio
import requests, pytest
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS
from API_project.utils.fixture_utils import admin_token, auth_headers

@pytest.fixture
def user(auth_headers, role: str = "passenger"):

    user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "full_name": fake.name(),
        "role": role
    }

    user_modification = {
        "email": fake.email(),
        "password": fake.password(),
        "full_name": fake.name()
    }

    r = requests.post(f"{BASE_URL}{USERS}", json=user_data, headers=auth_headers, timeout=5)
    r.raise_for_status()
    user_created = r.json()
    yield user_created
    requests.put(f"{BASE_URL}{USERS}/{user_created['id']}", json=user_modification, headers=auth_headers, timeout=5)
    requests.delete(f"{BASE_URL}{USERS}/{user_created['id']}", headers=auth_headers, timeout=5)





#crear otros fixture con datos fijos para poder utilizar para otros test, y despues no olvidar de borrarlos

def test_user_creation_update_deletion(user, auth_headers):
    print(user)

def test_admin_token(admin_token):
    return admin_token

