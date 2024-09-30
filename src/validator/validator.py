from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def validate(self, timestamp: str, temperature: float) -> bool:
        pass


class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(f"Validation Error: {message}")


class DuplicateError(Exception):
    def __init__(self, message):
        super().__init__(f"Duplicated Error: {message}")
