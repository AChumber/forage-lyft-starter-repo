from datetime import datetime
from typing import List

from engine.sternman_engine import SternmanEngine
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tire.CarriganTires import CarriganTires
from tire.OctoprimeTires import OctoprimeTires
from car import Car


class CarFactory:

    @staticmethod
    def create_calliope(current_date: datetime,
                        last_service_date: datetime,
                        current_mileage: int,
                        last_service_mileage: int,
                        tire_wear_readings: List[float]) -> Car:
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        carrigan_tires = CarriganTires(tire_wear_readings)
        return Car(capulet_engine, spindler_battery, carrigan_tires)

    @staticmethod
    def create_glissade(current_date: datetime,
                        last_service_date: datetime,
                        current_mileage: int,
                        last_service_mileage: int,
                        tire_wear_readings: List[float]) -> Car:
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        carrigan_tires = CarriganTires(tire_wear_readings)
        return Car(willoughby_engine, spindler_battery, carrigan_tires)

    @staticmethod
    def create_palindrome(current_date: datetime,
                          last_service_date: datetime,
                          is_warning_light_on: bool,
                          tire_wear_readings: List[float]) -> Car:
        sternman_engine = SternmanEngine(is_warning_light_on)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        octoprime_tires = OctoprimeTires(tire_wear_readings)
        return Car(sternman_engine, spindler_battery, octoprime_tires)

    @staticmethod
    def create_rorschach(current_date: datetime,
                         last_service_date: datetime,
                         current_mileage: int,
                         last_service_mileage: int,
                         tire_wear_readings: List[float]) -> Car:
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        octoprime_tires = OctoprimeTires(tire_wear_readings)
        return Car(willoughby_engine, nubbin_battery, octoprime_tires)

    @staticmethod
    def create_thovex(current_date: datetime,
                      last_service_date: datetime,
                      current_mileage: int,
                      last_service_mileage: int,
                      tire_wear_readings: List[float]) -> Car:
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        carrigan_tires = CarriganTires(tire_wear_readings)
        return Car(capulet_engine, nubbin_battery, carrigan_tires)
