from domain.interfaces import IBatteryRepository, IAudioRepository, IAlarmConfigRepository
from domain.entities import BatteryState, AlarmSettings
from data.battery_service import BatteryService
from data.audio_service import AudioService

class BatteryRepository(IBatteryRepository):
    def __init__(self, battery_service: BatteryService):
        self._service = battery_service

    def get_current_state(self) -> BatteryState:
        return self._service.check_hardware_status()

class AudioRepository(IAudioRepository):
    def __init__(self, audio_service: AudioService):
        self._service = audio_service

    def play_sound(self, file_path: str) -> None:
        self._service.play(file_path)

    def stop_sound(self) -> None:
        self._service.stop()

class MemoryAlarmConfigRepository(IAlarmConfigRepository):
    def __init__(self):
        self._settings = AlarmSettings(is_enabled=False, audio_path=None)

    def save_settings(self, settings: AlarmSettings) -> None:
        self._settings = settings

    def load_settings(self) -> AlarmSettings:
        return self._settings