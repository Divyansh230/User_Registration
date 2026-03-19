from utils.first_name_util import first_name_utils

def validate_user(user):

    if not first_name_utils(user.first_name):
        return f'{user} first name is invalid'
    
    else:
        return f'{user} is valid'