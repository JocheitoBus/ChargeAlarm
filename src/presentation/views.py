import flet as ft
import flet_audio as fta
import time
import threading
from presentation.view_models import AlarmViewModel

class AlarmView(ft.Container):
    def __init__(self, page: ft.Page, view_model: AlarmViewModel):
        super().__init__()

        self.main_page = page
        self.vm = view_model
        self.default_audio = None

        self.on_mount = self._on_mount
        
        # ELEMENTOS
        self.title = ft.Container(
            ft.Text(
                "TITULAZO",
                width=320,
                size=30,
                text_align="center",
                weight="w900"
            )
        )
        self.alarm_text = ft.Text(
            "ACTIVAR MODO\nALARMA",
            width=200,
            size=30,
            text_align="center",
            weight="w900"
        )
        self.alarm_button = ft.Container(
            self.alarm_text,
            width=260,
            height=260,
            border_radius=130,
            bgcolor=ft.Colors.RED_200,
            alignment=ft.Alignment.CENTER,
            on_click=self._on_alarm_click
        )
        

        self.content = ft.Column([
            self.title,
            self.alarm_button
        ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        self.width = 320
        self.height = 500
        self.bgcolor = ft.Colors.DEEP_ORANGE_ACCENT
        self.border_radius = 20

    def _on_mount(self, e):
        if self.default_audio is None:
            self.default_audio = fta.Audio(
                src=self.vm.alarm_use_case.load_saved_data().audio_path,
                autoplay=False,
                volume=1.0,
                release_mode="loop"
            )
            self.main_page.services.append(self.default_audio)
            self.main_page.update() 
            
            self.vm.alarm_use_case.init_audio(self.default_audio)


        self.vm.bind_ui(self.render)

        threading.Thread(target=self._auto_refresh, daemon=True).start()
        self.render()

    def render(self):
        # Boton Activar Alarma
        enabled = self.vm.alarm_use_case.load_saved_data().is_enabled
        charging = self.vm.battery_use_case.execute().is_charging
        if enabled:
            self.alarm_text.value = "DESACTIVAR\nALARMA"
            if charging:
                self.alarm_button.bgcolor = ft.Colors.GREEN
            else:
                self.alarm_button.bgcolor = ft.Colors.RED
        else:
            if charging:
                self.alarm_text.value = "CARGANDO"
                self.alarm_button.bgcolor = ft.Colors.GREEN_400
            else:
                self.alarm_text.value = "SIN\nCORRIENTE"
                self.alarm_button.bgcolor = ft.Colors.GREY

            
        self.update()

    def _auto_refresh(self):
        while True:
            try:
                if not self.main_page or self.main_page.session is None:
                    break

                self.render()
                self.vm.alarm_use_case.check_plugged(self.vm.battery_use_case.execute())
            except Exception:
                pass
            time.sleep(1)

    # EVENTOS
    def _on_alarm_click(self, e):
        self.vm.toggle_alarm()