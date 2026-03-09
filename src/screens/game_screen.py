from textual.screen import Screen
from textual.widgets import Footer, Digits, Label
from textual.reactive import reactive

from src.utils.temp_save_load import Temp
from src.game.grinding import Grind

class GameScreen(Screen):
    coins: reactive[int] = reactive(0)
    grind: Grind = Grind(0.5, 1)
    BINDINGS = [
        ("space", "press_space", "to get coins"),
        ("escape", "press_escape", "to main menu"),
    ]

    def __init__(self, new_game: bool = True, **kwargs):
        super().__init__(**kwargs)
        self.new_game = new_game

    def compose(self):
        yield Digits(id="counter")
        yield Footer()

    def on_mount(self) -> None:
        if self.new_game:
            self.coins = 0
        else:
            self.coins = Temp.load()

    def watch_coins(self, coins: str):
        validated_coins = max(0, coins)
        self.query_one("#counter", Digits).update(f"{validated_coins}")

    def action_press_space(self):
        self.coins = self.grind.grind(self.coins)

    def action_press_escape(self) -> None:
        Temp.save(self.coins)
        self.app.switch_screen("Menu")
