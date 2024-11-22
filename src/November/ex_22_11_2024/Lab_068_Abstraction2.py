"""
# Abstraction:
"""
from abc import ABC, abstractmethod


class PyATB(ABC):

    @abstractmethod
    def pay_fee(self):
        pass

    def enroll(self):
        print("Enrolled")

class Student1(PyATB):

    def pay_fee(self):
        print("Paid")

enroll_student = Student1()
enroll_student.enroll()