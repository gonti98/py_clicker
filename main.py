from textual.app import App, ComposeResult
from textual.widgets import Footer

from src.screens.main_menu import MainMenu

class MyGameApp(App):
    CSS_PATH = "assets/style.tcss"
    COMMAND_PALETTE_BINDING = "question_mark"
    SCREENS = {
        "Menu": MainMenu,
    }

    def on_mount(self) -> None:
        self.push_screen("Menu")

if __name__ == "__main__":
    app = MyGameApp()
    app.run()
