import random
import string
import datetime
import requests, pytest
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS
from API_project.utils.fixture_utils import admin_token, auth_headers



@pytest.fixture
def flight(auth_headers):
    flight_data = {
  "origin": "".join(random.choices(string.ascii_uppercase, k=3)),
  "destination": "".join(random.choices(string.ascii_uppercase, k=3)),
  "departure_time": fake.date_time(tzinfo=datetime.timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z'),
  "arrival_time": fake.date_time(tzinfo=datetime.timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z'),
  "base_price": round(fake.pyfloat(left_digits=3, right_digits=2, positive=True), 2),
  "aircraft_id": fake.bothify(text='???-###')
}
    r = requests_with_error_handling(method="POST", url=BASE_URL + FLIGHTS, json=flight_data, headers=auth_headers, timeout=5)
    # r = requests.post(BASE_URL + FLIGHTS, json=flight_data, headers=auth_headers, timeout=5)
    # try:
    #     r.raise_for_status()
    # except Exception as e:
    #     try:
    #         print(r.text())
    #     except:
    #         pass
    #     raise e
    flight_response = r.json() #crea una variable con el json de la response
    yield flight_response #para probar el airport_response en el mismo fixture

    requests.delete(f'{BASE_URL}{FLIGHTS}/{flight_response["id"]}', headers=auth_headers, timeout=5)


#crear otros fixture con datos fijos para poder utilizar para otros test, y despues no olvidar de borrarlos

def test_flight(flight):
    print(flight)