from datetime import datetime
from random import randint, random


class DataGenerator:
    def get_timestamp(self):
        return (datetime.now().isoformat(),)

    def get_temperature(self):
        return randint(100000, 400000) / 10000
