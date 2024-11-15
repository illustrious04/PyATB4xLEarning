"""
Create an Bank account management program
1) Create Bank account with taking user input (Name, Account number, current balance
2) Perform Deposit, withdraw, check balance, and exit from the process.
"""
from random import choice


class BankAccount():
    def __init__(self, account_holder , account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

# Creating Method for deposit amount
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New Balance {self.balance}")
        else:
            print("Invalid deposit amount!")

# Creating Method to withdraw the amount
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid or insufficient funds!")

    def display_balance(self):
        print(f"Current Balance: {self.balance}")

# Main Program--
# Taking user input to create an account
print("Welcome to the Bank")
account_holder = input("Enter your Name: ")
account_number = int(input("Enter your account number: "))
initial_balance = float(input("Enter your account balance: "))

# Create the bank account

account = BankAccount(account_holder,account_number,initial_balance)

#Menu Loop
while True:
    print("\n1. Deposit 2. Withdraw 3. Check Balance 4. Exit")
    choice = input("Chose an Option")

    if choice == "1":
        amount = float(input("Enter Deposit Amount: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter withdrawal Amount: "))
        account.withdraw(amount)
    elif choice == "3":
        account.display_balance()
    elif choice == "4":
        print("Thank you for banking with us")
        break
    else:
        print("Invalid option try again!")






























