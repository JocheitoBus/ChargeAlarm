import os
import json
from domain.interfaces import IAlarmConfigRepository
from domain.entities import AlarmSettings

class AlarmConfigRepository(IAlarmConfigRepository):
    def __init__(self, file_path):
        self.file_path = file_path

    def save_settings(self, settings: AlarmSettings) -> None:
        try:
            data_to_save = {
                "is_enabled": settings.is_enabled,
                "audio_path": settings.audio_path
            }
            
            folder = os.path.dirname(self.file_path)
            if folder:
                os.makedirs(folder, exist_ok=True)

            with open(self.file_path, "w") as file:
                json.dump(data_to_save, file, indent=4)
            
        except Exception as e:
            print(f"Infraestructura: [ERROR] No se pudo guardar la configuración: {str(e)}")
    
    def load_settings(self) -> AlarmSettings:
        audio_path = "/audio/alarm.m4a"

        if not os.path.exists(self.file_path):
            return AlarmSettings(is_enabled=False, audio_path=audio_path)
        
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                return AlarmSettings(
                    is_enabled=data.get("is_enabled", False),
                    audio_path=data.get("audio_path", audio_path)
                )
        except Exception:
            return AlarmSettings(is_enabled=False, audio_path=audio_path)