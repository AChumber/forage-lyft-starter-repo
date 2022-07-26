import unittest
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        cur_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(cur_mileage, last_service_mileage)

        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        cur_mileage = 29999
        last_service_mileage = 0
        engine = CapuletEngine(cur_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())

    def test_engine_with_no_miles_should_not_be_serviced(self):
        cur_mileage = 0
        last_service_mileage = 0
        engine = CapuletEngine(cur_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=True)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=False)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        cur_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(cur_mileage, last_service_mileage)

        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        cur_mileage = 59999
        last_service_mileage = 0
        engine = WilloughbyEngine(cur_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())

    def test_engine_with_no_miles_should_not_be_serviced(self):
        cur_mileage = 0
        last_service_mileage = 0
        engine = CapuletEngine(cur_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())
