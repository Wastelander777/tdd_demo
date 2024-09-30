from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def validate(self, timestamp: str, temperature: float) -> bool:
        pass
