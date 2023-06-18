POST_SCHEMA = {
    "type": "object",
    "properties":
        {
            "body": {"type": "string"},
            "id": {"type": "number"},
            "title": {"type": "string"},
            "userId": {"type": "number"}
        },
    "required": ["body", "id", "title", "userId"]
}
