import re

def first_name_utils(name):
    pattern=r'^[A-Z][a-zA-Z]{2,}$'
    return bool(re.match(pattern,name))