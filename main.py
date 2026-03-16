from textual.app import App, ComposeResult

from src.config.bindings import BINDINGS, GlobalActions
from src.screens.game_screen import GameScreen
from src.screens.main_menu import MainMenu
from src.screens.settings_menu import SettingsMenu


class MyGameApp(GlobalActions, App):
    ESCAPE_TO_MINIMIZE = False
    NOTIFICATION_TIMEOUT = 2
    CSS_PATH = [
        "assets/style.tcss",
        "assets/confirmation_modal.tcss",
    ]
    COMMAND_PALETTE_BINDING = "question_mark"
    BINDINGS = BINDINGS["global"]
    SCREENS = {
    "Game": GameScreen,
    "Menu": MainMenu,
    "Settings": SettingsMenu,
    }

    def on_mount(self) -> None:
        self.push_screen("Menu")


if __name__ == "__main__":
    app = MyGameApp()
    app.run()
