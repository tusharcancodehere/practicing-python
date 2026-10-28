import sqlite3

class Bank:
    def __init__(self, name,balance):
        self.name = name
        self.balance = balance
    def greet(self):
        print("==============")
        print("Welcome to Bank")
        print("==============")
    def create_account(self,balance=1000):
        while True:
            user_input_name = input("Please enter your name: ")
            user_confirmation = input("Please enter your confirmation(y/n): ")

            if user_confirmation == "y":
                # Save the input values to the object instance
                self.name = user_input_name
                self.balance = balance
                print(f"Account successfully created for {self.name} with a balance of {self.balance}!")

                break  # <--- This breaks out of the loop and exits the function naturally

        print("Let's try again...\n")
    def deposit(self, amount):
        pass
    def withdraw(self, amount):
        pass
    def transfer(self, amount):
        pass
    def withdrawal(self, amount):
        pass
    def history(self):
        pass
