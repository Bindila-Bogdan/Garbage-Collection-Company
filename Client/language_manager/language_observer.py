from abc import ABC, abstractmethod


class LanguageObserver(ABC):
    @abstractmethod
    def update(self, dictionary, index):
        pass
