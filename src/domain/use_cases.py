from domain.config_repository import AlarmConfigRepository
from domain.audio_repository import AudioRepository
from domain.battery_repository import BatteryRepository
from domain.entities import AlarmSettings, BatteryState

class MonitorBatteryUseCase:
    def __init__(self, battery_repo: BatteryRepository):
        self._battery_repo = battery_repo

    def execute(self) -> BatteryState:
        return self._battery_repo.get_current_state()

class ManageAlarmUseCase:
    def __init__(self, audio_repo: AudioRepository, config_repo: AlarmConfigRepository):
        self._audio_repo = audio_repo
        self._config_repo = config_repo

    def init_audio(self, flet_audio_instance):
        self._audio_repo.init_audio(flet_audio_instance)

    def check_plugged(self, battery: BatteryState):
        if not battery.is_charging:
            self._audio_repo.stop_alarm()

    def load_saved_data(self):
        return self._config_repo.load_settings()
    
    def save_data(self, settings: AlarmSettings):
        return self._config_repo.save_settings(settings)

    def get_alarm_state(self, battery_state: BatteryState) -> bool:
        settings = self.load_saved_data()
        if settings.is_enabled and battery_state.is_charging:
            return True
        return False

    def trigger_alarm_if_charging(self, battery_state: BatteryState, settings: AlarmSettings) -> bool:
        if self.get_alarm_state(battery_state):
            if settings.audio_path:
                self._audio_repo.play_alarm()
                return True
        return False

    def stop_alarm(self) -> None:
        self._audio_repo.stop_alarm()