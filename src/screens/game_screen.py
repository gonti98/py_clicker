import time
from textual.screen import Screen
from textual.widgets import Footer, Digits, Label
from textual.reactive import reactive

from src.config.bindings import BINDINGS
from src.utils.save_manager import SaveManager
from src.game.grinding import Grind

class GameScreen(Screen):
    BINDINGS = BINDINGS["GameScreen"]
    coins: reactive[int] = reactive(0)
    grind = Grind()

    def __init__(self, new_game: bool = True, **kwargs):
        super().__init__(**kwargs)
        self.new_game = new_game
        self.start_time = time.time()
        self.total_playtime = 0.0

    def compose(self):
        yield Digits(id="counter")
        yield Label(id="info")
        yield Footer()

    def on_mount(self):
        if self.new_game:
            self.reset_game()
        else:
            game_state = SaveManager.load_game()
            if game_state is not None:
                self.coins = game_state["coins"]
                self.grind = game_state["grind"]
                self.total_playtime = game_state["metadata"].get("total_playtime", 0.0)
            else:
                self.reset_game()
        self.watch_coins(self.coins)

    def reset_game(self):
        self.coins = 0
        self.grind = Grind()

    def watch_coins(self, coins: int):
        coins_display = max(0, coins)
        self.query_one("#counter", Digits).update(f"{coins_display:g}")
        upgrade_cost = self.grind.next_income_upgrade_cost
        info = self.query_one("#info", Label)
        info.update(f"Income: {self.grind.income_per_click} (Cost: {self.grind.next_income_upgrade_cost}) | "
        f"Cooldown: {self.grind.cooldown:.2}s (Cost: {self.grind.next_cooldown_upgrade_cost})")

    def action_press_space(self):
        self.coins = self.grind.click(self.coins)
    def action_press_1(self):
        self.coins = self.grind.income_upgrade(self.coins)
    def action_press_2(self):
        self.coins = self.grind.cooldown_upgrade(self.coins)

    def action_press_escape(self):
        session_time = time.time() - self.start_time
        self.total_playtime += session_time
        SaveManager.save_game(self.coins, self.grind, self.total_playtime)
        self.app.switch_screen("Menu")
