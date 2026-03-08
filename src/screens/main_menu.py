from textual.screen import Screen
from textual.containers import Center, CenterMiddle
from textual.widgets import Button, Label

from assets.logo import TITLE_ASCII
from src.screens.game_screen import GameScreen
from src.utils.temp_save_load import Temp

class MainMenu(Screen):
    def compose(self):
        yield Center(Label(TITLE_ASCII, id="logo"))
        yield CenterMiddle(
            Button("Continue", id="continue", disabled=True),
            Button("Start", id="start"),
            Button("Settings", id="settings"),
            id="menu",
        )

    def on_mount(self) -> None:
        continue_btn = self.query_one("#continue", Button)
        continue_btn.disabled = not Temp.SAVE_FILE.exists()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        match button_id:
            case "continue":
                self.app.notify("Continue!")
            case "start":
                self.app.push_screen("Game")
            case "settings":
                self.app.notify("Settings!")
            case _:
                self.app.notify(f"Error: {button_id}")
