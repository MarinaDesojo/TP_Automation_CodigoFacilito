import requests, pytest
from API_project.utils.config import ADMIN_USER, ADMIN_PASS
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS

# Loguea y extrae el access_token para poder continuar con otros tests
@pytest.fixture(scope="session")
def admin_token() -> str: # yo espero que la función me devuelva un string
    r = requests.post(BASE_URL + AUTH_LOGIN,
                      data={"username": ADMIN_USER, "password": ADMIN_PASS},
                      timeout=5)
    r.raise_for_status() #da error en caso de que no devuelva 200
    return r.json()["access_token"]

# Este fixture retorna el token listo para los headers de otras peticiones
@pytest.fixture
def auth_headers(admin_token):
    return {"Authorization": f"Bearer {admin_token}"}



def test_admin_token(admin_token):
    return admin_token
