import re


def es_email_correcto(email: str):
    email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if re.fullmatch(email_pattern, email):
        return True
    else:
        return False
