import pytest, requests, os
from jsonschema import validate, ValidationError
from test_schema import flight_schema
from API_project.utils.settings import fake, BASE_URL, AUTH_LOGIN, USERS, AIRPORTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRCRAFTS

def test_create_flight_schema(flight):
    validate(instance=flight, schema=flight_schema)


def test_get_all_flights(flight, auth_headers):
    #va con data, origin, destination, date, skip y limit
    r = requests.get(f"{BASE_URL}{FLIGHTS}", headers=auth_headers)
    assert r.status_code == 200 #si quiero ver lo que hay en lista tengo que poner el breakpoing en esta linea, frena antes de ejecutar la linea donde se colocar
    assert r.text != "" #esto verifica que el texto dentro del response no se encuentre vecio, ver en debug
