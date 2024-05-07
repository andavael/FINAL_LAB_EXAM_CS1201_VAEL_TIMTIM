from user import *

class UserManager:
    def load_user():
        pass
    def save_users():
        pass
    def validate_username():
        pass
    def validate_password():
        pass
    def register():
        print("REGISTER USER")
        user = {}
        username = input("Please enter a username or leave blank to exit: ")
        while True:
            try:
                if not username:
                    exit()
                if len(username) < 4:
                    print("Username must at least be four characters. Please enter a new one.")
                    return
                if username in user:
                    print("Username must at least be four characters. Please enter a new one.")
                else: 
                    password = input("Please enter a password or leave blank to exit: ")
                    if not password:
                        exit()
                    if len(password) < 8:
                        print("Password must be at least eight characters. Please enter a new one.")
                        return
            except ValueError as e:
                print (e) 
    def login():
        print("USER LOGIN")
        while True:
            try:
                username = input("Please enter username or leave blank to exit.")
                password = input("Please enter password.")
                if username in users 

            except ValueError as e:
                print (e)


        