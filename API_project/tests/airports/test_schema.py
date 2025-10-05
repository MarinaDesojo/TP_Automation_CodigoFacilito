import random, string
from API_project.utils.settings import fake

airport_schema = {
    "type": "object",
    "required": ["iata_code", "city", "country"],
    "properties": {
        "iata_code": {"type": "string", "minlength": 3, "maxlength": 3},
        "city": {"type": "string"},
        "country": {"type": "string"}
    },
    "additionalProperties": False
}

airport_schema_array = {
    "type": "array",
    "items": airport_schema
}

random_airport_data = {
      "iata_code": "".join(random.choices(string.ascii_uppercase, k=3)),
      "city": "La Paz",
      "country": fake.country_code()
    }

bad_airport_data = [{
      "iata_code": "MM",
      "city": "Oslo",
      "country": "Noruega"
    },
    {
      "iata_code": "MMMM",
      "city": "Oslo",
      "country": "Noruega"
    },
    {
      "iata_code": "123",
      "city": "Oslo",
      "country": "Noruega"
    },
    {
      "iata_code": "!AA",
      "city": "Oslo",
      "country": "Noruega"
    },
    {
      "iata_code": "/AA",
      "city": "Oslo",
      "country": "Noruega"
    },
    {
      "iata_code": ".AA",
      "city": "Oslo",
      "country": "Noruega"
    },
    {
      "iata_code": 123,
      "city": "Oslo",
      "country": "Noruega"
    },
    {
      "iata_code": "AAA",
      "city": 123,
      "country": "Noruega"
    },
    {
      "iata_code": "AAA",
      "city": "Oslo",
      "country": 123
    },
    {
      "iata_code": "@AA",
      "city": "Oslo",
      "country": "Noruega"
    },
    {
      "iata_code": "#AA",
      "city": "Oslo",
      "country": "Noruega"
    },
    {
      "iata_code": "",
      "city": "",
      "country": ""
    },
    {
      "iata_code": " ",
      "city": " ",
      "country": " "
    }

    ]

good_airport_data = {
      "iata_code": "MMM",
      "city": "Oslo",
      "country": "Noruega"
    }

changed_airport_data = {
      "iata_code": "MMM",
      "city": "Madrid",
      "country": "España"
    }

changed_airport_data_iata_code = {
      "iata_code": "NNN",
      "city": "Madrid",
      "country": "España"
    }

good_airport_data_1 = {
    "iata_code": "MMM",
    "city": "Oslo",
    "country": "Noruega"
}

good_airport_data_2 = {
    "iata_code": "NNN",
    "city": "Madrid",
    "country": "España"
}

