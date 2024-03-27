GetSingleResource = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                },
                "year": {
                    "type": "integer"
                },
                "color": {
                    "type": "string"
                },
                "pantone_value": {
                    "type": "string"
                }
            },
            "additionalProperties": False,
            "required": [
                "id",
                "name",
                "year",
                "color",
                "pantone_value"
            ]
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string"
                },
                "text": {
                    "type": "string"
                }
            },
            "additionalProperties": False,
            "required": [
                "url",
                "text"
            ]
        }
    },
    "additionalProperties": False,
    "required": [
        "data",
        "support"
    ]
}
