from src.validator.validator import ValidationError, Validator


class InputValidator(Validator):
    def validate(self, timestamp: str, temperature: float):
        if not all([isinstance(temperature, float), isinstance(timestamp, str)]):
            raise ValidationError("Entered data does not have the expect format")
        return True
