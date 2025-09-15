import pytest, requests
from jsonschema import validate, ValidationError

booking_schema = {
    "type": "object",
    "required": ["flight_id", "passengers"],
    "properties": {
        "flight_id": {
            "type": "string"
        },
        "passengers": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["full_name", "passport", "seat"],
                "properties": {
                    "full_name": {"type": "string"},
                    "passport": {"type": "string"},
                    "seat": {"type": "string"}
                },
                "additionalProperties": False
            },
            "minItems": 1
        }
    },
    "additionalProperties": False
}
