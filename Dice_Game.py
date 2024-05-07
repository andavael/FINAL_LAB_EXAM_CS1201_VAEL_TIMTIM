import datetime
import random
from User_Manager import *
from user import *


class DiceGame:
    def __init__(self, cpu, player):
        self.player = player
        self.cup = cpu
    def load_resources():
        pass
    def save_score():
        pass
    def play_game():
        print("1. Start Game")
        print("2. History")
        print("3. Logout")
        game_choice = input(int("Enter your choice or leave blank to exit."))

        while True:
            try:
                if game_choice == 1:
                    pass
                elif game_choice == 2: 
                    pass  
                elif game_choice == 3:
                    pass

            except ValueError as e:
                print (e) 
    def show_top_scores():
        pass
    def logout():
        pass

def menu():
    print("Welcome to Dice Game!")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input(int("Enter your choice or leave blank to exit."))

    while True:
        try:
            if choice == 1:
                User_Manager.register()
            elif choice == 2:
                User_Manager.login()
            elif choice == 3:
                exit()
            else: 
                print("Invalid choice, Please enter a valid input.")
        except ValueError as e:
            print (e)
menu()

class 