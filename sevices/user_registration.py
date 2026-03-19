from utils.registration_util import validate_first_name
from utils.registration_util import validate_last_name
from utils.registration_util import validate_email
from utils.registration_util import validate_phone

def validate_user(user):

    if not validate_first_name(user.first_name):
        raise ValueError(f'{user} Invalid First Name')
    
    elif not validate_last_name(user.last_name):
        raise ValueError(f'{user} Invalid Last Name')
    
    elif not validate_email(user.email):
        raise ValueError(f'{user} Email is invalid')
    
    elif not validate_phone(user.phone_number):
        raise ValueError(f'{user} phone number is invalid')
    
    else:
        return f'{user} is valid'