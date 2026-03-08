from textual.app import App, ComposeResult
from textual.widgets import Footer

from src.screens.main_menu import MainMenu
from src.screens.game_screen import GameScreen


class MyGameApp(App):
    CSS_PATH = "assets/style.tcss"
    COMMAND_PALETTE_BINDING = "question_mark"
    SCREENS = {
        "Menu": MainMenu,
        "Game": GameScreen,
            }

    def get_default_screen(self) -> Screen:
        return MainMenu()

if __name__ == "__main__":
    app = MyGameApp()
    app.run()
