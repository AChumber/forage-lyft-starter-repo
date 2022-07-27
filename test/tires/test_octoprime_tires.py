import unittest
from tire.OctoprimeTires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tires = OctoprimeTires([0.8, 0.9, 0.6, 0.9])  # sum = 3.2
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tires = OctoprimeTires([0.52, 0.66, 0.26, 0.0])  # sum = 1.44
        self.assertFalse(tires.needs_service())
