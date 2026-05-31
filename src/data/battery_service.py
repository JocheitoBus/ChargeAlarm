import psutil
from domain.entities import BatteryState

class BatteryService:
    def check_hardware_status(self) -> BatteryState:
        try:
            sensors = psutil.sensors_battery()
            if sensors is None:
                return BatteryState(is_charging=False, percentage=50)
            
            return BatteryState(
                is_charging=sensors.power_plugged,
                percentage=int(sensors.percent)
            )
        except Exception:
            return BatteryState(is_charging=False, percentage=0)