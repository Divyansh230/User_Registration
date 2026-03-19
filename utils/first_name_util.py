import re

def validate_first_name(name):
    pattern=r'^[A-Z][a-zA-Z]{2,}$'
    return bool(re.match(pattern,name))