import random, string, datetime
from API_project.utils.settings import fake

flight_schema = {
    "type": "object",
    "required": ["origin", "destination", "departure_time", "arrival_time", "base_price", "aircraft_id", "id", "available_seats"],
    "properties": {
        "origin": {"type": "string", "minlength": 3, "maxlength": 3},
        "destination": {"type": "string", "minlength": 3, "maxlength": 3},
        "departure_time": {"type": "string", "format": "date-time"},
        "arrival_time": {"type": "string", "format": "date-time"},
        "base_price": {"type": "number"},
        "aircraft_id": {"type": "string"},
        "id": {"type": "string"},
        "available_seats": {"type": "integer"}
    },
    "additionalProperties": False
}

flight_schema_array = {
    "type": "array",
    "items": flight_schema
}

departure = fake.date_time(tzinfo=datetime.timezone.utc)

random_flight_data = {
    "origin": "".join(random.choices(string.ascii_uppercase, k=3)),
    "destination": "".join(random.choices(string.ascii_uppercase, k=3)),
    "departure_time": departure.isoformat().replace('+00:00', 'Z'),
    "arrival_time": (departure + datetime.timedelta(hours=2)).isoformat().replace('+00:00', 'Z'),
    "base_price": round(fake.pyfloat(left_digits=3, right_digits=2, positive=True), 2),
    "aircraft_id": fake.bothify(text='???-###')
}

bad_flight_scenarios = [
    {
        "name": "arrival_before_departure",
        "departure_time": departure.isoformat().replace('+00:00', 'Z'),
        "arrival_time": (departure - datetime.timedelta(hours=2)).isoformat().replace('+00:00', 'Z'),
        "base_price": 100.0
    },
    {
        "name": "negative_base_price",
        "departure_time": departure.isoformat().replace('+00:00', 'Z'),
        "arrival_time": (departure + datetime.timedelta(hours=2)).isoformat().replace('+00:00', 'Z'),
        "base_price": -50.0
    },
    {
        "name": "arrival_equals_departure",
        "departure_time": departure.isoformat().replace('+00:00', 'Z'),
        "arrival_time": departure.isoformat().replace('+00:00', 'Z'),
        "base_price": 200.0
    },
    {
        "name": "base_price string",
        "departure_time": departure.isoformat().replace('+00:00', 'Z'),
        "arrival_time": (departure + datetime.timedelta(hours=2)).isoformat().replace('+00:00', 'Z'),
        "base_price": "500"
    },
    {
        "name": "base_price string2",
        "departure_time": departure.isoformat().replace('+00:00', 'Z'),
        "arrival_time": (departure + datetime.timedelta(hours=2)).isoformat().replace('+00:00', 'Z'),
        "base_price": "zero"
    },
    {
        "name": "future datetime format departure",
        "departure_time": "19001-01-01 15:25:00Z",
        "arrival_time": (departure + datetime.timedelta(hours=2)).isoformat().replace('+00:00', 'Z'),
        "base_price": 50.0
    },
    {
        "name": "future datetime format arrival",
        "departure_time": departure.isoformat().replace('+00:00', 'Z'),
        "arrival_time": "19001-01-01 15:25:00Z",
        "base_price": 50.0
    },
    {
        "name": "past datetime format arrival",
        "departure_time": departure.isoformat().replace('+00:00', 'Z'),
        "arrival_time": "191-01-01 15:25:00Z",
        "base_price": 50.0
    },
    {
        "name": "past datetime format departure",
        "departure_time": "191-01-01 15:25:00Z",
        "arrival_time": (departure + datetime.timedelta(hours=2)).isoformat().replace('+00:00', 'Z'),
        "base_price": 50.0
    },
    {
        "name": "departure_time int",
        "departure_time": 1900,
        "arrival_time": (departure + datetime.timedelta(hours=2)).isoformat().replace('+00:00', 'Z'),
        "base_price": 50.0
    },
    {
        "name": "arrival_time int",
        "departure_time": departure.isoformat().replace('+00:00', 'Z'),
        "arrival_time": 1900,
        "base_price": 50.0
    }
]

