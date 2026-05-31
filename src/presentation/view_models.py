import threading
import time
import traceback
from domain.use_cases import MonitorBatteryUseCase, ManageAlarmUseCase

class AlarmViewModel:
    def __init__(self, battery_use_case: MonitorBatteryUseCase, alarm_use_case: ManageAlarmUseCase):
        self.battery_use_case = battery_use_case
        self.alarm_use_case = alarm_use_case
        
        self._ui_callback = None
        self._play_audio_callback = None
        self._stop_audio_callback = None

    def bind_ui(self, callback):
        self._ui_callback = callback

    def update_ui(self):
        try:
            if self._ui_callback:
                self._ui_callback()
        except Exception as e:
            pass

    def get_alarm_state(self) -> bool:
        battery = self.battery_use_case.execute()
        return self.alarm_use_case.get_alarm_state(battery)

    def toggle_alarm(self):
        settings = self.alarm_use_case.load_saved_data()

        settings.is_enabled = not settings.is_enabled
        self.alarm_use_case.save_data(settings)
        
        if not settings.is_enabled:
            self.alarm_use_case.stop_alarm()

        self.update_ui()
        self.start_background_monitoring()

    def start_background_monitoring(self):
        threading.Thread(target=self._worker, daemon=True).start()

    def _worker(self):
        settings = self.alarm_use_case.load_saved_data()
        while settings.is_enabled:
            try:
                battery = self.battery_use_case.execute()
                self.alarm_use_case.trigger_alarm_if_charging(battery,settings)
            except Exception as e:
                traceback.print_exc()
                self.battery_info = f"Error de lectura: {str(e)}"
            
            self.update_ui()
            time.sleep(2)