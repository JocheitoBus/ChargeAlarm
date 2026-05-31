import os
import json
import psutil
from abc import ABC, abstractmethod
from domain.entities import BatteryState, AlarmSettings

class IBatteryRepository(ABC):
    @abstractmethod
    def get_current_state(self) -> BatteryState:
        pass

class IAudioRepository(ABC):
    @abstractmethod
    def play_alarm(self, file_path: str) -> None:
        pass
    
    @abstractmethod
    def stop_alarm(self) -> None:
        pass

class IAlarmConfigRepository(ABC):
    @abstractmethod
    def save_settings(self, settings: AlarmSettings) -> None:
        pass
            
    
    @abstractmethod
    def load_settings(self) -> AlarmSettings:
        pass