from engine.engine import Engine


class CapuletEngine(Engine):
    SERVICE_MILEAGE_THRESHOLD = 30000

    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > self.SERVICE_MILEAGE_THRESHOLD
