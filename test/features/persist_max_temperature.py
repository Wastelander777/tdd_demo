import unittest

from src.usecase.persist_max_temperature import PersistMaxTemperature


class TestPersistMaxTemperature(unittest.TestCase):
    def setUp(self):
        self.persist_max_temperature = PersistMaxTemperature()

    def test_validate_with_valid_float(self):
        self.assertTrue(self.persist_max_temperature.validate(23.5))
        self.assertTrue(self.persist_max_temperature.validate(-10.0))
        self.assertTrue(self.persist_max_temperature.validate(0.0))

    def test_validate_with_invalid_input(self):
        with self.assertRaises(ValueError):
            self.persist_max_temperature.validate("25.5")
        with self.assertRaises(ValueError):
            self.persist_max_temperature.validate(True)
        with self.assertRaises(ValueError):
            self.persist_max_temperature.validate([20.5])
        with self.assertRaises(ValueError):
            self.persist_max_temperature.validate(None)

    if __name__ == "__main__":
        unittest.main()
