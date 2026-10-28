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
        pass

    def withdraw(self, amount:float):
        # 1. Check
        # if the user actually has enough money in the database
        self.cursor.execute("SELECT balance FROM accounts WHERE name = ?", (self.name,))
        result = self.cursor.fetchone()

        if result is None:
            print("Error: Account not found in database.")
            return

        current_db_balance = result[0]

        # 2. Prevent overdrafting
        if amount > current_db_balance:
            print(f"Transaction Denied! Insufficient funds. Your current balance is: {current_db_balance}")
            return

        # 3. Calculate new balance and update the SQLite table
        new_balance = current_db_balance - amount
        self.cursor.execute(
            "UPDATE accounts SET balance = ? WHERE name = ?",
            (new_balance, self.name)
        )
        self.conn.commit()

        # 4. Synchronize the local object instance tracking variable
        self.balance = new_balance
        print(f"Successfully withdrew ${amount}. New balance is: ${self.balance}")


    def transfer(self, amount):
        pass

    def withdrawal(self, amount):
        pass

    def history(self):
        pass
