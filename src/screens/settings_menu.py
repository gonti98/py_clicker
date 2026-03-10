from textual.screen import Screen
from textual.widgets import Footer

class SettingsMenu(Screen):
    BINDINGS = [
        ("escape", "press_escape", "to main menu"),
    ]

    def compose(self):
        yield Footer()

    def action_press_escape(self) -> None:
        self.app.switch_screen("Menu")
