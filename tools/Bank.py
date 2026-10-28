import sqlite3


class Bank:
    def __init__(self, db_name="bank.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.name = None
        self.balance = 0.0

        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS accounts
                            (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                balance REAL NOT NULL
                            )
                            ''')
        self.conn.commit()

    @staticmethod
    def greet():
        print("==============\nWelcome to Bank\n==============")

    def create_account(self, balance=1000):
        while True:
            user_input_name = input("Please enter your name: ")
            user_confirmation = input("Please enter your confirmation(y/n): ")

            if user_confirmation == "y":
                self.cursor.execute(
                    "INSERT INTO accounts (name, balance) VALUES (?, ?)",
                    (user_input_name, balance)
                )
                self.conn.commit()

                self.name = user_input_name
                self.balance = balance
                print(f"Account successfully created for {self.name} with a balance of {self.balance}!")
                break

            print("Let's try again...\n")

    def deposit(self, amount):
        if not self.name:
            print("Error: Please create an account first.")
            return
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return
        
        self.balance += amount

    def withdraw(self, amount):
        pass

    def transfer(self, amount):
        pass

    def withdrawal(self, amount):
        pass

    def history(self):
        pass
