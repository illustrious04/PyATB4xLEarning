"""
# Abstraction:
* Hide the details and show what is required
* This is on Class level
* Actual meaning of Abstract is Incomplete.
* We can use the Abstract method by importing it "from abc import ABC, abstractclassmethod"
"""
from abc import ABC, abstractmethod


class Father(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass

class Son(Father):

    def loan(self):
        print("Loan is paid by the Son")

son1 = Son("1Lakh")
son1.loan()