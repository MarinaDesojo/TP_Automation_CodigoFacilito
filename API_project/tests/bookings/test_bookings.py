import pytest, requests, os
from jsonschema import validate, ValidationError
from test_schema import booking_schema
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS

def test_create_booking_schema(booking):
    validate(instance=booking, schema=booking_schema)


def test_get_all_bookings(booking, auth_headers):
    r = requests.get(f"{BASE_URL}{BOOKINGS}", headers=auth_headers)
    assert r.status_code == 200 #si quiero ver lo que hay en lista tengo que poner el breakpoing en esta linea, frena antes de ejecutar la linea donde se colocar
    assert r.text != "" #esto verifica que el texto dentro del response no se encuentre vecio, ver en debug
