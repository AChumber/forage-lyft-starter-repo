from tire.tire import Tire


class CarriganTires(Tire):

    def __init__(self, tire_wear_readings):
        self.tire_wear_readings = tire_wear_readings

    def needs_service(self) -> bool:
        # serviced when one or more value >= 0.9
        for tire_wear in self.tire_wear_readings:
            if tire_wear >= 0.9:
                return True

        return False
