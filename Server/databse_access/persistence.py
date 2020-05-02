from abc import ABC, abstractmethod


class Persistence(ABC):
    def __init__(self, name):
        self.__persistence_name = name

    @abstractmethod
    def get_data(self):
        pass
