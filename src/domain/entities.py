from dataclasses import dataclass
from typing import Optional

@dataclass
class BatteryState:
    is_charging: bool
    percentage: int

@dataclass
class AlarmSettings:
    is_enabled: bool
    audio_path: Optional[str] = None