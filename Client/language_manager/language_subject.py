from abc import ABC, abstractmethod


class LanguageSubject(ABC):
    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass
