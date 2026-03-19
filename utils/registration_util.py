import re

def validate_first_name(name):
    pattern=r'^[A-Z][a-zA-Z]{2,}$'
    return bool(re.match(pattern,name))

def validate_last_name(last_name):
    pattern=r'^[A-Z][a-zA-Z]{2,}$'
    return bool(re.match(pattern,last_name))

def validate_email(email):
      pattern = r'^[a-zA-Z0-9]+([._+-][a-zA-Z0-9]+)*@[a-zA-Z0-9]+(\.[a-zA-Z]{2,}){1,2}$'
      return bool(re.match(pattern, email))

def validate_phone(phone):
    pattern=r'^\d{2} \d{10}$'
    return bool(re.match(pattern,phone))


def validate_password(password):
    if len(password)<8:
        print('Paswword Length should be greater than 8')
        return False
    
    if not re.search(r'[A-Z]',password):
        return False
    
    if not re.search(r'[0-9]',password):
        return False
    
