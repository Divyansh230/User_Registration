from models.user import User
from sevices.user_registration import validate_user

class Main:

    
    def main():
        print('This is User Registration Problem')

        user=User('divyansh','singh','divyanshsinghh2304@gmail.com','1244213690','helloWorld')
        print(validate_user(user))

    if __name__=='__main__':
        main()