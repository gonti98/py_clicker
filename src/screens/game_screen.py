import time
from textual.reactive import reactive
from textual.screen import Screen
from textual.widgets import Digits, Footer, Label

from src.config.bindings import BINDINGS, GameActions
from src.game.buildings import BUILDINGS, Building
from src.game.grinding import Grind
from src.utils.save_manager import SaveManager


class GameScreen(GameActions, Screen):
    BINDINGS = BINDINGS["GameScreen"]

    def __init__(self, new_game: bool = True, **kwargs):
        super().__init__(**kwargs)
        self.new_game = new_game
        self.start_time = time.time()
        self.total_playtime = 0.0

    def compose(self):
        yield Digits(id="counter")
        yield Label(id="grinding")
        yield Label(id="buildings")
        yield Footer()

    def reset_game(self):
        self.coins = 0
        self.grind = Grind()
        for building in BUILDINGS.values():
            building.count = 0

    def on_mount(self):
        if self.new_game:
            self.reset_game()
        else:
            game_state = SaveManager.load_game()
            if game_state is not None:
                self.coins = game_state["coins"]
                self.grind = game_state["grind"]
                self.total_playtime = game_state["metadata"].get("total_playtime", 0.0)
                self.buildings = game_state["buildings"]
                BUILDINGS.update(self.buildings)
            else:
                self.reset_game()
        self.set_interval(1/60, self.update_counter)
        self.set_interval(1.0, self.game_tick)
        self.set_interval(0.1, self.update_ui)

    def game_tick(self):
        total_income = 0
        for building in BUILDINGS.values():
            total_income += building.get_income_per_second()
        self.coins += int(total_income)

    def update_counter(self):
        coins_display = max(0, self.coins)
        self.query_one("#counter", Digits).update(f"{coins_display:.5g}💰")

    def update_ui(self):
        grind_label = self.query_one("#grinding", Label)
        grind_label.update(
            f"Income: {self.grind.income_per_click:.5g} "
            f"(Cost: {self.grind.next_income_upgrade_cost:.5g}) | "
            f"Cooldown: {self.grind.cooldown:.2f}s "
            f"(Cost: {self.grind.next_cooldown_upgrade_cost:.5g})"
        )
        buildings_label = self.query_one("#buildings", Label)
        building_infos = []
        for name, building in BUILDINGS.items():
            income = int(building.get_income_per_second())
            cost = building.get_cost()
            building_infos.append(
                f"{name}: {building.count} (Income: {income:.5g}, Cost: {cost:.5g})"
            )
        buildings_label.update("\n".join(building_infos))

    def action_press_escape(self):
        session_time = time.time() - self.start_time
        self.total_playtime += session_time
        SaveManager.save_game(self.coins, self.grind, BUILDINGS, self.total_playtime)
        self.app.switch_screen("Menu")
