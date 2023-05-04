from relay_controller import RelayController


class PumpControl:

    def __init__(self, watering_time):
        self.watering_time = watering_time

    def water_plants(self, interval: float):
        RelayController().activate(interval)