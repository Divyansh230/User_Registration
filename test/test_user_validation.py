import pytest
import os  
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.user import User
from sevices.user_registration import validate_user


##Valid User Test

def test_valid_user():
    user=User(
        'Divyansh',
        'Singh',
        'divyansh.signh2304@gmail.com'
        "91 9919819801",
        "Password1@"
    )

    assert validate_user(user) == f'{user} is valid'


## First name Test
@pytest.mark.parametrize("first_name,expected",[
    ("Di", "Invalid First Name"), # less than 3 chars
    ("divyansh", "Invalid First Name"), # not capitalized
    ("D1v", "Invalid First Name"), # contains digit
])

def test_invalid_first_name(first_name,expected):
    user=User(first_name,'Singh',"abc@yahoo.com", "91 9919819801", "Password1@")
    assert validate_user(user)==expected

## Last name Test
@pytest.mark.parametrize("last_name, expected", [
    ("si", "Invalid Last Name"),
    ("singh", "Invalid Last Name"),
    ("S1n", "Invalid Last Name"),
])

def test_invalid_last_name(last_name, expected):
    user = User("Divyansh", last_name, "abc@yahoo.com", "91 9919819801", "Password1@")
    assert validate_user(user) == expected

## Email test

@pytest.mark.parametrize("email, expected", [
    ("abc", "Invalid Email"),
    ("abc@.com", "Invalid Email"),
    ("abc123@gmail.a", "Invalid Email"),
    ("abc..2002@gmail.com", "Invalid Email"),
    ("abc@gmail.com.1a", "Invalid Email"),
])
def test_invalid_email(email, expected):
    user = User("Divyansh", "Singh", email, "91 9919819801", "Password1@",)
    assert validate_user(user) == expected


## Phone Test
@pytest.mark.parametrize("phone, expected", [
    ("919919819801", "Invalid Phone"), # no space
    ("91 991981980", "Invalid Phone"), # less digits
    ("91-9919819801", "Invalid Phone"), # wrong format
])
def test_invalid_phone(phone, expected):
    user = User("Divyansh", "Singh", "abc@yahoo.com", phone, "Password1@")
    assert validate_user(user) == expected


## Password Test

@pytest.mark.parametrize("password, expected", [
    ("Pass1@", "Invalid Password"), # less than 8 chars
    ("password1@", "Invalid Password"), # no uppercase
    ("PASSWORD@", "Invalid Password"), # no number
    ("Password1@@", "Invalid Password"), # more than 1 special char
    ])
def test_invalid_password(password, expected):
    user = User("Divyansh", "Singh", "abc@yahoo.com", "91 9919819801", password)
    assert validate_user(user) == expected