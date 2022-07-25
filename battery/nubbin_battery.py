from battery.battery import Battery


class NubbinBattery(Battery):
    SERVICE_THRESHOLD = 4

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        year_since_last_service = self.last_service_date.year - self.current_date.year
        return year_since_last_service >= self.SERVICE_THRESHOLD
