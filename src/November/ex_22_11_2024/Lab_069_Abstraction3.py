"""
# Abstraction:
"""
from abc import ABC, abstractmethod


class Engine(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Engine):

    def start(self):
        print("Engine Started")

    def stop(self):
        print("Car has stopped")

    def drive(self):
        self.start()
        print("Car is Driving")
        self.stop()



alto = Car()
alto.drive()