import unittest
from datetime import datetime
from car_factory import CarFactory


class TestCalliopeCar(unittest.TestCase):

    def test_engine_should_need_service(self):
        car = CarFactory.create_calliope(
            datetime.today(),
            datetime.today().replace(year=datetime.today().year - 1),
            31000,
            0,
            [0.2, 0.1, 0.3, 0.23]
        )

        self.assertTrue(car.needs_service())

    def test_battery_should_need_service(self):
        car = CarFactory.create_calliope(
            datetime.today(),
            datetime.today().replace(year=datetime.today().year - 4),
            4000,
            0,
            [0.2, 0.1, 0.3, 0.23]
        )

        self.assertTrue(car.needs_service())

    def test_tires_should_need_service(self):
        car = CarFactory.create_calliope(
            datetime.today(),
            datetime.today().replace(year=datetime.today().year - 1),
            4000,
            0,
            [0.8, 0.85, 0.912, 0.85]
        )

        self.assertTrue(car.needs_service())

    def test_car_should_not_need_service(self):
        car = CarFactory.create_calliope(
            datetime.today(),
            datetime.today().replace(year=datetime.today().year - 1),
            4000,
            0,
            [0.8, 0.85, 0.75, 0.85]
        )

        self.assertFalse(car.needs_service())