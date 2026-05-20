class Azienda:
    def __init__(self, id, name, coord):
        self.__id = id
        self.__name = name
        self.__coord = coord

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def coord(self):
        return self.__coord