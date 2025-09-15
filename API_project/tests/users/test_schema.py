import pytest, requests
from attr.validators import max_len
from jsonschema import validate, ValidationError

user_schema = {
    "type": "object",
    "required": ["id", "email", "full_name", "role"],
    "properties": {
        "id": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "full_name": {"type": "string"},
        "role": {"type": "string", "enum": ["admin", "passenger"]},
    },
    "additionalProperties": True #password es una propiedad adicional
}


