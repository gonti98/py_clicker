from src.config.bindings import SettingsMenuActions, BINDINGS
from textual.screen import Screen
from textual.widgets import Footer


class SettingsMenu(SettingsMenuActions, Screen):
    BINDINGS = BINDINGS["SettingsMenu"]

    def compose(self):
        yield Footer()

    def action_press_escape(self) -> None:
        self.app.switch_screen("Menu")
