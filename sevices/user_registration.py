from utils.first_name_util import validate_first_name
from utils.last_name_util import validate_last_name

def validate_user(user):

    if not validate_first_name(user.first_name):
        raise ValueError(f'{user} Invalid First Name')
    
    elif not validate_last_name(user.last_name):
        raise ValueError(f'{user} Invalid Last Name')
    
    else:
        return f'{user} is valid'