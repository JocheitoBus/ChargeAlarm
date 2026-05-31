import psutil
from domain.interfaces import IBatteryRepository
from domain.entities import BatteryState

class BatteryRepository(IBatteryRepository):
    def __init__(self):
        super().__init__()

    def get_current_state(self) -> BatteryState:
        battery_sensor = psutil.sensors_battery()
        chargig = battery_sensor.power_plugged if battery_sensor else False
        percentage = battery_sensor.percent if battery_sensor else 0

        return BatteryState(is_charging=chargig,percentage=percentage)