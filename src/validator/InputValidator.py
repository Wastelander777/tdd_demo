from src.validator.validator import Validator


class InputValidator(Validator):
    def validate(self, timestamp: str, temperature: float):
        return all([isinstance(temperature, float), isinstance(timestamp, str)])
