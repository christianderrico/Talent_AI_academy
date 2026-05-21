class IdGen:
    def __init__(self, start = 0):
        self.__start = start

    def next(self):
        self.__start += 1
        return self.__start