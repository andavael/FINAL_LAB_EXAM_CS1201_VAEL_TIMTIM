from User_Manager import *

class User_manager:
    def user():
        pass











def main():
    print("Welcome to Dice Game!")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input(int("Enter your choice or leave blank to exit."))

    while True:
        try:
            if choice == 1:
                self.register()
            elif choice == 2:
                self.login()
            elif choice == 3:
                exit()
        except ValueError as e:
            print (e)

if __name__ == "__main__":
    main()