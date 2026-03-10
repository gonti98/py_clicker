from textual.screen import Screen
from textual.containers import Center, CenterMiddle
from textual.widgets import Button, Label

from assets.logo import TITLE_ASCII
from src.config.bindings import BINDINGS
from src.screens.game_screen import GameScreen
from src.screens.settings_menu import SettingsMenu
from src.utils.temp_save_load import Temp

class MainMenu(Screen):
    BINDINGS = BINDINGS["MainMenu"]

    def compose(self):
        yield Center(Label(TITLE_ASCII, id="logo"))
        yield CenterMiddle(
            Button("Continue", id="continue", disabled=True),
            Button("New Game", id="start_new_game"),
            Button("Settings", id="settings"),
            Button("Quit", id="quit"),
            id="menu",
        )

    def on_screen_resume(self) -> None:
        self.update_continue_button()

    def update_continue_button(self):
        has_save = Temp.TEMP_SAVE_FILE.exists()
        continue_btn = self.query_one("#continue", Button)
        continue_btn.disabled = not has_save
        if has_save:
            continue_btn.focus()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        match button_id:
            case "continue":
                self.app.switch_screen(GameScreen(new_game=False))
            case "start_new_game":
                self.app.switch_screen(GameScreen())
            case "settings":
                self.app.switch_screen(SettingsMenu())
            case "quit":
                self.app.exit()
            case _:
                self.app.notify(f"Error: {button_id}")
