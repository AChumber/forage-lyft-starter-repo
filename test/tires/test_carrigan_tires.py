import unittest
from tire.CarriganTires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tires = CarriganTires([0.52, 0.66, 0.26, 0.93])
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tires = CarriganTires([0.52, 0.66, 0.26, 0.0])
        self.assertFalse(tires.needs_service())
