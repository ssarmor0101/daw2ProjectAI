from abc import ABC, abstractmethod

class TranslatorIA(ABC):

    @abstractmethod
    def translate(self, text: str, source: str, target: str) -> str:
        pass
