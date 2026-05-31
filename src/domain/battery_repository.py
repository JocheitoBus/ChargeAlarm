import sys
from domain.interfaces import IBatteryRepository
from domain.entities import BatteryState
try:
    import psutil
except ImportError:
    psutil = None

class BatteryRepository(IBatteryRepository):
    def __init__(self):
        super().__init__()

    def is_plugged_in(self) -> bool:
        if sys.platform != "android":
            if psutil and psutil.sensors_battery():
                return psutil.sensors_battery().power_plugged
            return False

        else:
            try:
                if self.page:
                    return self.page.platform_interfaces.battery.is_charging()
            except Exception:
                pass
            
            return False

    def get_current_state(self) -> BatteryState:
        battery_sensor = psutil.sensors_battery()
        chargig = self.is_plugged_in
        percentage = battery_sensor.percent if battery_sensor else 0

        return BatteryState(is_charging=chargig,percentage=percentage)