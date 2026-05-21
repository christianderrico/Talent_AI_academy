from enum import Enum


class Status(Enum):
    AVAILABLE = "Available"
    IN_USE = "In use"
    BROKEN = "Broken"


class VehicleType(Enum):
    BYCICLE = "Bycicle"
    TRUCK = "Truck"
    ELECTRICSCOOTER = "Electric Scooter"
    CAR = "Car"


class DrivingLicense(Enum):
    A = "A"
    B = "B"
    C = "C"


class Vehicle:
    def __init__(self, id, name, driving_license, maximum_weight):
        self.__id = id
        self.__name = name
        self.__driving_license = driving_license
        self.__status = Status.AVAILABLE
        self.__weight = 0
        self.__maximum_weight = maximum_weight

    @property
    def maximum_weight(self):
        return self.__maximum_weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def _weight(self, value):
        self.__weight = value

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
        super().__init__(
            id,
            name=VehicleType.BYCICLE,
            driving_license=None,
            maximum_weight=10
        )


class ElectricScooter(Vehicle):
    def __init__(self, id):
        super().__init__(
            id,
            name=VehicleType.ELECTRICSCOOTER,
            driving_license=DrivingLicense.A,
            maximum_weight=40,
        )


class Car(Vehicle):
    def __init__(self, id):
        super().__init__(
            id,
            name=VehicleType.CAR,
            driving_license=DrivingLicense.B,
            maximum_weight=150,
        )


class Truck(Vehicle):
    def __init__(self, id):
        super().__init__(
            id,
            name=VehicleType.TRUCK,
            driving_license=DrivingLicense.C,
            maximum_weight=500,
        )
