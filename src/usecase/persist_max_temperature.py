class PersistMaxTemperature:
    def __init__(self):
        pass

    def validate(self, temperature: float, timestamp: str):
        return isinstance(temperature, float) and isinstance(timestamp, str)

    def persist(self):
