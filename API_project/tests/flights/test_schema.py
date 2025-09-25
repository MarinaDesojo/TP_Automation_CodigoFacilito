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

random_flight_data = {
    "origin": "".join(random.choices(string.ascii_uppercase, k=3)),
    "destination": "".join(random.choices(string.ascii_uppercase, k=3)),
    "departure_time": fake.date_time(tzinfo=datetime.timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z'),
    "arrival_time": fake.date_time(tzinfo=datetime.timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z'),
    "base_price": round(fake.pyfloat(left_digits=3, right_digits=2, positive=True), 2),
    "aircraft_id": fake.bothify(text='???-###')
}

bad_flight_data = [{
    "origin": "",
    "destination": "",
    "departure_time": "",
    "arrival_time": "",
    "base_price": "",
    "aircraft_id": ""
    },
    {
      "tail_number": "1234",
      "model": "B 40",
      "capacity": 40
    },
    {
      "tail_number": "12345678910",
      "model": "B 40",
      "capacity": 40
    },
    {
      "tail_number": "1234567",
      "model": 40,
      "capacity": 40
    },
    {
      "tail_number": "1234567",
      "model": "B 40",
      "capacity": "40"
    },
    {
      "tail_number": "1234567",
      "model": "B 40",
      "capacity": 1000
    }
    # ,
    # {
    #   "tail_number": "1234567",
    #   "model": "B 40",
    #   "capacity": 40
    # },
    # {
    #   "tail_number": "1234567",
    #   "model": "B 40",
    #   "capacity": 40
    # },
    # {
    #   "tail_number": "1234567",
    #   "model": "B 40",
    #   "capacity": 40
    # },
    # {
    #   "tail_number": "1234567",
    #   "model": "B 40",
    #   "capacity": 40
    # },
    # {
    #   "tail_number": "1234567",
    #   "model": "B 40",
    #   "capacity": 40
    # },
    # {
    #   "tail_number": "1234567",
    #   "model": "B 40",
    #   "capacity": 40
    # },
    # {
    #   "tail_number": "1234567",
    #   "model": "B 40",
    #   "capacity": 40
    # }
    ]

good_flight_data = {
      "tail_number": "123AB",
      "model": "B 40",
      "capacity": 40
    }

changed_flight_data = {
      "tail_number": "45678910CD",
      "model": "D-750",
      "capacity": 150
    }


