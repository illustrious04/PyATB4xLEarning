# Live example of Encapsulation

class Bank:
    def __init__(self, account_number, balance):
        self.balance = balance
        self.__account_number = account_number

    def deposite(self, amount):
        self.balance = self.balance+amount

    def check_balance(self):
        print(self.balance)

    def show_account_number(self, is_auth):
        if is_auth == True:
            print(self.balance)
        else:
            print("Not Allowed.")
# Private methods can access the private variable and public method also protected as well.
# this is not allwed to access outside the class
    def __internal_Method(self):
        print("This is a private method")
        print(self.__account_number)

HDFC = Bank(7224092225, 200)
HDFC.deposite(100)
HDFC.check_balance()
HDFC.show_account_number(False)




