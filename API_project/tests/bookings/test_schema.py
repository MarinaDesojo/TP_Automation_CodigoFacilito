import random
from API_project.utils.settings import fake

booking_schema = {
    "type": "object",
    "required": ["id", "flight_id", "user_id", "status", "passengers"],
    "properties": {
        "id": {"type": "string"},
        "flight_id": {"type": "string"},
        "user_id": {"type": "string"},
        "status": {"type": "string", "enum": ["draft", "paid", "checked_in", "cancelled"]},
        "passengers": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["full_name", "passport", "seat"],
                "properties": {
                    "full_name": {"type": "string"},
                    "passport": {"type": "string"},
                    "seat": {"type": ["string", "null"]}
                },
                "additionalProperties": False
            },
            "minItems": 1
        }
    },
    "additionalProperties": False
}

booking_schema_array = {
    "type": "array",
    "items": booking_schema
}

good_booking_passenger_data = [{
    "full_name": "Pepe",
    "passport": "ASD6513513",
    "seat": "57F"
}]

random_booking_passenger_data = [
    {
        "full_name": fake.name(),
        "passport": fake.bothify(text='??######'),
        "seat": f"{random.randint(1, 60)}{random.choice(['A', 'B', 'C', 'D', 'E', 'F'])}"
    },{
        "full_name": fake.name(),
        "passport": fake.bothify(text='??######'),
        "seat": None
    }
]

bad_booking_passenger_data = [[
    {
        "full_name": "",
        "passport": "UL545879541",
        "seat": "45A"
    }
],
[
    {
        "full_name": " ",
        "passport": "UL545879541",
        "seat": "45A"
    }
],
[
    {
        "full_name": "Julieta Gonzalez",
        "passport": "",
        "seat": "45A"
    }
],
[
    {
        "full_name": "Julieta Gonzalez",
        "passport": " ",
        "seat": "45A"
    }
],
[
    {
        "full_name": "Julieta Gonzalez",
        "passport": "UL545879541",
        "seat": ""
    }
],
[
    {
        "full_name": "Julieta Gonzalez",
        "passport": "UL545879541",
        "seat": " "
    }
],
[
    {
        "full_name": 123456,
        "passport": "UL545879541",
        "seat": "45A"
    }
],
[
    {
        "full_name": "Julieta Gonzalez",
        "passport": 123456126,
        "seat": "45A"
    }
],
[
    {
        "full_name": "Julieta Gonzalez",
        "passport": "UL545879541",
        "seat": 45
    }
],
[
    {
        "full_name": None,
        "passport": "UL545879541",
        "seat": "45A"
    }
],
[
    {
        "full_name": "Julieta Gonzalez",
        "passport": None,
        "seat": "45A"
    }
]
]

