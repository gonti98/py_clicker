from textual.app import App, ComposeResult

from src.config.bindings import BINDINGS

class MyGameApp(App):
    BINDINGS = BINDINGS["global"]
    CSS_PATH = "assets/style.tcss"
    COMMAND_PALETTE_BINDING = "question_mark"
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
