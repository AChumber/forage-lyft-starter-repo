from engine.engine import Engine


class WilloughbyEngine(Engine):
    SERVICE_MILEAGE_THRESHOLD = 60000

    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > self.SERVICE_MILEAGE_THRESHOLD
