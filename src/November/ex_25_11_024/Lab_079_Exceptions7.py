"""
# Custom Exceptions Handling:
* User defined exception

"""

class My_custom_exceptio(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

balance = 100
withdraw = int(input("Enter the amount you want to withdraw: \n"))

if withdraw > balance:
    raise My_custom_exceptio("Balance is low")
else:
    print("Remaining Bal", (balance-withdraw))















































