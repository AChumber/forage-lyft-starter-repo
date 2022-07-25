from datetime import datetime

from engine.engine import Engine
from engine.sternman_engine import SternmanEngine
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.battery import Battery
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from car import Car


class CarFactory:

    @staticmethod
    def __create_capulet_engine(current_mileage, last_service_mileage) -> Engine:
        return CapuletEngine(current_mileage, last_service_mileage)

    @staticmethod
    def __create_willoughby_engine(current_mileage, last_service_mileage) -> Engine:
        return WilloughbyEngine(current_mileage, last_service_mileage)

    @staticmethod
    def __create_sternman_engine(warning_light_is_on) -> Engine:
        return SternmanEngine(warning_light_is_on)

    @staticmethod
    def __create_spindler_battery(last_service_date, current_date) -> Battery:
        return SpindlerBattery(last_service_date, current_date)

    @staticmethod
    def __create_nubbin_battery(last_service_date, current_date) -> Battery:
        return NubbinBattery(last_service_date, current_date)

    @staticmethod
    def create_calliope(current_date: datetime,
                        last_service_date: datetime,
                        current_mileage: int,
                        last_service_mileage: int) -> Car:
        capulet_engine = CarFactory.__create_capulet_engine(current_mileage, last_service_mileage)
        spindler_battery = CarFactory.__create_spindler_battery(last_service_date, current_date)

        return Car(capulet_engine, spindler_battery)

    @staticmethod
    def create_glissade(current_date: datetime,
                        last_service_date: datetime,
                        current_mileage: int,
                        last_service_mileage: int) -> Car:
        willoughby_engine = CarFactory.__create_willoughby_engine(current_mileage, last_service_mileage)
        spindler_battery = CarFactory.__create_spindler_battery(last_service_date, current_date)
        return Car(willoughby_engine, spindler_battery)

    @staticmethod
    def create_palindrome(current_date: datetime,
                          last_service_date: datetime,
                          is_warning_light_on: bool) -> Car:
        sternman_engine = CarFactory.__create_sternman_engine(is_warning_light_on)
        spindler_battery = CarFactory.__create_spindler_battery(last_service_date, current_date)
        return Car(sternman_engine, spindler_battery)

    @staticmethod
    def create_rorschach(current_date: datetime,
                         last_service_date: datetime,
                         current_mileage: int,
                         last_service_mileage: int) -> Car:
        willoughby_engine = CarFactory.__create_willoughby_engine(current_mileage, last_service_mileage)
        nubbin_battery = CarFactory.__create_nubbin_battery(last_service_date, current_date)
        return Car(willoughby_engine, nubbin_battery)

    @staticmethod
    def create_thovex(current_date: datetime,
                         last_service_date: datetime,
                         current_mileage: int,
                         last_service_mileage: int) -> Car:
        capulet_engine = CarFactory.__create_capulet_engine(current_mileage, last_service_mileage)
        nubbin_battery = CarFactory.__create_nubbin_battery(last_service_date, current_date)
        return Car(capulet_engine, nubbin_battery)