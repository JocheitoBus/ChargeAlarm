import flet as ft
from presentation.views import AlarmView
from presentation.view_models import AlarmViewModel

# REPOSITORIES
from domain.audio_repository import AudioRepository
from domain.config_repository import AlarmConfigRepository
from domain.battery_repository import BatteryRepository

# USE CASES
from domain.use_cases import *

def main(page: ft.Page):
    data_path = "alarm_config.json"

    battery_repo = BatteryRepository()
    audio_repo = AudioRepository()
    config_repo = AlarmConfigRepository(file_path=data_path)
    
    battery_use_case = MonitorBatteryUseCase(battery_repo)
    alarm_use_case = ManageAlarmUseCase(audio_repo,config_repo)

    view_model = AlarmViewModel(battery_use_case,alarm_use_case)
    views = AlarmView(page,view_model)

    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = ft.Colors.BLACK
    page.add(views)
    views.on_mount(None)

ft.run(
    main,
    assets_dir="assets"
)