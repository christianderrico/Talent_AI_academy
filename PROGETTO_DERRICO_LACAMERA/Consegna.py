from enum import Enum

class DeliveryStatus(Enum):
    CREATED = "Created"
    STARTED = "Started"
    COMPLETED = "Completed"

class Delivery:
    def __init__(self, id_rider, id_azienda, start, arrive, extra_info):
        self.__id_rider = id_rider
        self.__id_azienda = id_azienda
        self.__start = start
        self.__arrive = arrive
        self.__extra_info = extra_info
        self.__status = DeliveryStatus.CREATED

    @property
    def extra_info(self):
        return dict(self.__extra_info)

    @property
    def id_rider(self):
        return self.__id_rider

    @property
    def id_azienda(self):
        return self.__id_azienda

    @property
    def start(self):
        return self.__start

    @property
    def arrive(self):
        return self.__arrive

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_state):
        self.__status = new_state
