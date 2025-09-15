import random
import string
import requests, pytest
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS
from API_project.utils.fixture_utils import admin_token, auth_headers


def build_booking_data(num_passengers=1):
    booking = {
        "flight_id": fake.bothify(text='FL####'),  # Ej: FL1234
        "passengers": []
    }

    for _ in range(num_passengers):
        passenger = {
            "full_name": fake.name(),
            "passport": fake.bothify(text='??########'),  # Ej: AB12345678
            "seat": f"{random.randint(1, 40)}{random.choice('ABCDEF')}"  # Ej: 12A
        }
        booking["passengers"].append(passenger)

    return booking


@pytest.fixture
def booking(auth_headers):
    booking_data = build_booking_data(num_passengers=3)

    r = requests.post("https://cf-automation-airline-api.onrender.com/bookings", json=booking_data, headers=auth_headers, timeout=5)
    r.raise_for_status()
    booking_response = r.json() #crea una variable con el json de la response
    yield booking_response #para probar el booking_response en el mismo fixture

    requests.delete(f'{BASE_URL}{BOOKINGS}/{booking_response["id"]}', headers=auth_headers, timeout=5)


#crear otros fixture con datos fijos para poder utilizar para otros test, y despues no olvidar de borrarlos

def test_booking(booking):
    print(booking)
