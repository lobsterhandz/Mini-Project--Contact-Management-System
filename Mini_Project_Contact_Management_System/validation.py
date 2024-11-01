import re

def validate_phone(phone):
    return re.match(r"^\+?[0-9]{10,15}$", phone)

def validate_email(email):
    return re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)
