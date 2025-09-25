import random, string
from API_project.utils.settings import fake

aircraft_schema = {
    "type": "object",
    "required": ["tail_number", "model", "capacity", "id"],
    "properties": {
        "tail_number": {"type": "string", "minlength": 5, "maxlength": 10},
        "model": {"type": "string"},
        "capacity": {"type": "integer"},
        "id": {"type": "string"},
    },
    "additionalProperties": False
}

aircraft_schema_array = {
    "type": "array",
    "items": aircraft_schema
}

def generate_tail_number(min_len=5, max_len=10):
    length = random.randint(min_len, max_len)
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

random_aircraft_data = {
      "tail_number": generate_tail_number(),
      "model": fake.word(),
      "capacity": random.randint(0,1000)
    }

bad_aircraft_data = [{
      "tail_number": 1234567,
      "model": "B 40",
      "capacity": 40
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

good_aircraft_data = {
      "tail_number": "123AB",
      "model": "B 40",
      "capacity": 40
    }

changed_aircraft_data = {
      "tail_number": "45678910CD",
      "model": "D-750",
      "capacity": 150
    }


