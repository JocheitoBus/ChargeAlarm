import flet as ft

class AudioService:
    def __init__(self):
        self._player = None

    def set_player(self, audio_component: ft.Audio):
        self._player = audio_component

    def play(self, audio_uri: str) -> None:
        if self._player:
            self._player.src = audio_uri
            self._player.play()

    def stop(self) -> None:
        if self._player:
            self._player.stop()