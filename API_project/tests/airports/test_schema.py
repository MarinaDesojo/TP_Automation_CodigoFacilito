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

random_airport_data = {
      "iata_code": "".join(random.choices(string.ascii_uppercase, k=3)), #no se deberían repetir, su codigo es unico, codigo aleatorio de 3 letras
      "city": "La Paz", #una ciudad puede tener varios aeropuertos
      "country": fake.country_code() #faker para datos random mokeados
    }

bad_airport_data = [{
      "iata_code": "MM", #no se deberían repetir, su codigo es unico, codigo aleatorio de 3 letras
      "city": "Oslo", #una ciudad puede tener varios aeropuertos
      "country": "Noruega" #faker para datos random mokeados
    },
    {
      "iata_code": "MMMM", #no se deberían repetir, su codigo es unico, codigo aleatorio de 3 letras
      "city": "Oslo", #una ciudad puede tener varios aeropuertos
      "country": "Noruega" #faker para datos random mokeados
    }
    ]

good_airport_data = {
      "iata_code": "MMM", #no se deberían repetir, su codigo es unico, codigo aleatorio de 3 letras
      "city": "Oslo", #una ciudad puede tener varios aeropuertos
      "country": "Noruega" #faker para datos random mokeados
    }


changed_airport_data = {
      "iata_code": "MMM", #no se deberían repetir, su codigo es unico, codigo aleatorio de 3 letras
      "city": "Madrid", #una ciudad puede tener varios aeropuertos
      "country": "España" #faker para datos random mokeados
    }

