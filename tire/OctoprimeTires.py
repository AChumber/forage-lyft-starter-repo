from tire.tire import Tire


class OctoprimeTires(Tire):
    TIRE_WEAR_THRESHOLD = 3

    def __init__(self, tire_wear_readings):
        self.tire_wear_readings = tire_wear_readings

    def needs_service(self) -> bool:
        return sum(self.tire_wear_readings) >= self.TIRE_WEAR_THRESHOLD