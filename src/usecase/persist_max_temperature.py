class PersistMaxTemperature:
    def __init__(self):
        pass

    def validate(self, temperature: float):
        if not isinstance(temperature, (int, float)):
            raise ValueError("Temperature must be a number")
        return True
