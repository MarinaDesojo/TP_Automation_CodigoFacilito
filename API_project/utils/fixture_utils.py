import requests, pytest
from API_project.utils.config import ADMIN_USER, ADMIN_PASS
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS

@pytest.fixture(scope="session")
def admin_token() -> str:
    r = requests.post(BASE_URL + AUTH_LOGIN,
                      data={"username": ADMIN_USER, "password": ADMIN_PASS},
                      timeout=5)
    r.raise_for_status()
    return r.json()["access_token"]


@pytest.fixture
def auth_headers(admin_token):
    return {"Authorization": f"Bearer {admin_token}"}

# def test_admin_token(admin_token):
#     return admin_token
