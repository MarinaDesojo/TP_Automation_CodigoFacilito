import random, string, datetime
from API_project.utils.settings import fake

payment_schema = {
    "type": "object",
    "required": ["id", "booking_id", "status"],
    "properties": {
        "id": {"type": "string"},
        "booking_id": {"type": "string"},
        "status": {"type": "string",
            "enum": ["pending", "success", "fail"]
        }
    },
    "additionalProperties": False
}


payment_schema_array = {
    "type": "array",
    "items": payment_schema
}

good_payment_data = [{
    "full_name": "Pepe",
    "passport": "ASD6513513",
    "seat": "57F"
}]

random_payment_data = [
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

bad_payment_amount_method_data = [
    {
        "amount": -1,
        "payment_method": "card"
    },
    {
        "amount": "One",
        "payment_method": "card"
    },
    {
        "amount": 0,
        "payment_method": 150
    },
    {
        "amount": 0,
        "payment_method": ""
    },
    {
        "amount": 0,
        "payment_method": " "
    },
    {
        "amount": "",
        "payment_method": "card"
    }#,
    # {
    #     "amount": 0,
    #     "payment_method": ""
    # },
    # {
    #     "amount": 0,
    #     "payment_method": ""
    # },
    # {
    #     "amount": 0,
    #     "payment_method": ""
    # },
    # {
    #     "amount": 0,
    #     "payment_method": ""
    # },
    # {
    #     "amount": 0,
    #     "payment_method": ""
    # }
]