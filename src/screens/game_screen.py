from textual.screen import Screen
from textual.widgets import Footer, Digits, Label
from textual.reactive import reactive

from src.config.bindings import BINDINGS
from src.utils.temp_save_load import Temp
from src.game.grinding import Grind
from src.game.buildings import Building

class GameScreen(Screen):
    BINDINGS = BINDINGS["GameScreen"]
    coins: reactive[int] = reactive(0)
    grind = Grind(1.0, 1000)

    def __init__(self, new_game: bool = True, **kwargs):
        super().__init__(**kwargs)
        self.new_game = new_game
        self.hard_drive = Building(1.0, 1, 100)
        self.data_center = Building(2.0, 10, 1000)

    def compose(self):
        yield Digits(id="counter")
        yield Label(id="hard_drive")
        yield Label(id="data_center")
        yield Footer()

    def on_mount(self):
        if self.new_game:
            self.reset_game()
        else:
            self.coins = Temp.load()
        self.set_interval(0.1, self.update_income)
        self.watch_coins(self.coins)

    def reset_game(self):
        self.coins = 0
        self.hard_drive.count = 0
        self.data_center.count = 0

    def watch_coins(self, coins: int):
        coins_display = max(0, coins)
        self.query_one("#counter", Digits).update(f"{coins_display:g}")
        self.query_one("#hard_drive", Label).update(
            f"HardDrive x{self.hard_drive.count} | "
            f"Cost: {self.hard_drive.next_cost:g} | "
            f"Income: {self.hard_drive.income_per_sec_total:g}/s"
        )
        self.query_one("#data_center", Label).update(
            f"DataCenter x{self.data_center.count} | "
            f"Cost: {self.data_center.next_cost:g} | "
            f"Income: {self.data_center.income_per_sec_total:g}/s"
        )

    def update_income(self):
        self.coins = self.hard_drive.generate_income(self.coins)
        self.coins = self.data_center.generate_income(self.coins)

    def action_press_1(self):
        self.coins = self.hard_drive.buy(self.coins)

    def action_press_2(self):
        self.coins = self.data_center.buy(self.coins)

    def action_press_space(self):
        self.coins = self.grind.click(self.coins)

    def action_press_escape(self):
        Temp.save(self.coins)
        self.app.switch_screen("Menu")
