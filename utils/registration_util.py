import re

def validate_first_name(name):
    pattern=r'^[A-Z][a-zA-Z]{2,}$'
    return bool(re.match(pattern,name))

def validate_last_name(last_name):
    pattern=r'^[A-Z][a-zA-Z]{2,}$'
    return bool(re.match(pattern,last_name))

def validate_email(email):
    pattern = r'^[a-z]+([._+-]*[a-z0-9]+)*@[a-z0-9]+\.[a-z]{2,}(\.[a-z]{2,})?$'
    return bool(re.match(pattern,email))
