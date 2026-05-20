from enum import Enum


class Status(Enum):
    AVAILABLE = "Available"
    IN_USE = "In use"
    BROKEN = "Broken"

class DrivingLicense(Enum):
    A = "A"
    B = "B"
    C = "C"


class Vehicle:
    def __init__(self, id, name, driving_license):
        self.__id = id
        self.__name = name
        self.__driving_license = driving_license
        self.__status = Status.AVAILABLE

    def driving_license(self):
        return self.__driving_license

    def is_broken(self):
        return self.__status == Status.BROKEN

    def is_available(self):
        return self.__status == Status.AVAILABLE

    def is_in_use(self):
        return self.__status == Status.IN_USE

    def change_status(self, new_state):
        self.__status = new_state

    def __str__(self):
        return f"Veicolo: {self.__name}, id:{self.__id}, status: {self.__status}"


class Bicycle(Vehicle):
    def __init__(self, id):
        super().__init__(id, name="Bicycle", driving_license=None)

class ElectricScooter(Vehicle):
    def __init__(self, id):
        super().__init__(id, name="ElectricScooter", driving_license=DrivingLicense.A)
