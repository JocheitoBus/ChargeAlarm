import time
from domain.interfaces import IAudioRepository

class AudioRepository(IAudioRepository):
    def __init__(self):
        self._audio_control = None
        self.playing = False

    def init_audio(self, flet_audio_instance):
        self._audio_control = flet_audio_instance

    def play_alarm(self) -> None:
        if self.playing:
            return
        if self._audio_control:
            try:
                page = self._audio_control.page
                if page:
                    page.run_task(self._audio_control.seek, 0)
                    time.sleep(0.05)
                    page.run_task(self._audio_control.play)
                    self.playing = True
            except Exception as e:
                print(f"Infraestructura: [ERROR AUDIO PLAY] {e}")
        else:
            print("Infraestructura: [WARNING] Intento de reproducir audio, pero el hardware no está listo.")

    def stop_alarm(self) -> None:
        if not self.playing:
            return
        if self._audio_control:
            try:
                page = self._audio_control.page
                if page:
                    page.run_task(self._audio_control.pause)
                    self.playing = False
            except Exception as e:
                print(f"Infraestructura: [ERROR AUDIO PLAY] {e}")
        else:
            print("Infraestructura: [WARNING] Intento de reproducir audio, pero el hardware no está listo.")