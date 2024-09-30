from src.validator.InputValidator import InputValidator


class PersistMaxTemperature:
    def __init__(self):
        self.validator = InputValidator()

    def persist(self, timestamp: str, temperature: float):
        self.validator.validate(timestamp, temperature)
        return "Data Saved"
