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

    def compose(self):
        yield Digits(id="counter")
        yield Label(id="info")
        yield Footer()

    def on_mount(self):
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
        self.app.switch_screen("Menu")
