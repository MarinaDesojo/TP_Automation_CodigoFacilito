flight_schema = {
    "type": "object",
    "required": ["origin", "destination", "departure_time", "arrival_time", "base_price", "aircraft_id"],
    "properties": {
        "origin": {"type": "string", "minlength": 3, "maxlength": 3},
        "destination": {"type": "string", "minlength": 3, "maxlength": 3},
        "departure_time": {"type": "string", "format": "date-time"},
        "arrival_time": {"type": "string", "format": "date-time"},
        "base_price": {"type": "number"},
        "aircraft_id": {"type": "string"}
    },
    "additionalProperties": False
}
