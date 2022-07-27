import unittest
from datetime import datetime
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        cur_date = datetime.today()
        last_service_date = cur_date.replace(year=cur_date.year - 3)
        battery = SpindlerBattery(last_service_date, cur_date)

        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        cur_date = datetime.today()
        last_service_date = cur_date.replace(year=cur_date.year - 2)
        battery = SpindlerBattery(last_service_date, cur_date)

        self.assertFalse(battery.needs_service())

    def test_brand_new_battery_should_not_be_serviced(self):
        cur_date = datetime.today()
        last_service_date = cur_date
        battery = SpindlerBattery(last_service_date, cur_date)

        self.assertFalse(battery.needs_service())


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        cur_date = datetime.today()
        last_service_date = cur_date.replace(year=cur_date.year - 4)
        battery = NubbinBattery(last_service_date, cur_date)

        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        cur_date = datetime.today()
        last_service_date = cur_date.replace(year=cur_date.year - 1)
        battery = NubbinBattery(last_service_date, cur_date)

        self.assertFalse(battery.needs_service())

    def test_brand_new_battery_should_not_be_serviced(self):
        cur_date = datetime.today()
        last_service_date = cur_date
        battery = NubbinBattery(last_service_date, cur_date)

        self.assertFalse(battery.needs_service())