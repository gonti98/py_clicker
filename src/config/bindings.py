from src.game.buildings import BUILDINGS
from src.game.grinding import Grind


class GlobalActions:
    def action_focus_h(self) -> None:
        self.action_focus_previous(x=0, y=-1)

    def action_press_j(self) -> None:
        self.action_focus_next()

    def action_press_k(self) -> None:
        self.action_focus_previous()

    def action_focus_l(self) -> None:
        self.action_focus_next(x=0, y=1)


class GameActions:
    def action_press_space(self) -> None:
        self.coins = self.grind.click(self.coins)

    def action_press_u(self) -> None:
        self.coins = self.grind.income_upgrade(self.coins)

    def action_press_c(self) -> None:
        self.coins = self.grind.cooldown_upgrade(self.coins)

    def action_press_1(self) -> None:
        self.coins = BUILDINGS["meadow"].buy(self.coins)

    def action_press_2(self) -> None:
        self.coins = BUILDINGS["grove"].buy(self.coins)

    def action_press_3(self) -> None:
        self.coins = BUILDINGS["forge"].buy(self.coins)

    def action_press_4(self) -> None:
        self.coins = BUILDINGS["tower"].buy(self.coins)

    def action_press_5(self) -> None:
        self.coins = BUILDINGS["alchemist"].buy(self.coins)

    def action_press_6(self) -> None:
        self.coins = BUILDINGS["portal"].buy(self.coins)

    def action_press_7(self) -> None:
        self.coins = BUILDINGS["dragon"].buy(self.coins)

    def action_press_8(self) -> None:
        self.coins = BUILDINGS["citadel"].buy(self.coins)

    def action_press_9(self) -> None:
        self.coins = BUILDINGS["worldtree"].buy(self.coins)


class MainMenuActions:
    pass


class SettingsMenuActions:
    pass


BINDINGS = {
    "global": [
        ("h", "focus_left", "Left"),
        ("j", "press_j", "Down"),
        ("k", "press_k", "Up"),
        ("l", "focus_right", "Right"),
    ],
    "GameScreen": [
        ("escape", "press_escape", "to main menu"),
        ("space", "press_space", "To get coins"),
        ("u", "press_u", "To upgrade click income"),
        ("c", "press_c", "To upgrade click cooldown"),
        ("1", "press_1", "Buy Meadow"),
        ("2", "press_2", "Buy Grove"),
        ("3", "press_3", "Buy Forge"),
        ("4", "press_4", "Buy Tower"),
        ("5", "press_5", "Buy Alchemist"),
        ("6", "press_6", "Buy Portal"),
        ("7", "press_7", "Buy Dragon"),
        ("8", "press_8", "Buy Citadel"),
        ("9", "press_9", "Buy Worldtree"),
    ],
    "MainMenu": [
        ("c", "press_c", "Continue"),
        ("n", "press_n", "New game"),
        ("s", "press_s", "Settings"),
        ("q", "press_q", "Quit"),
    ],
    "SettingsMenu": [
        ("escape", "press_escape", "to main menu"),
    ],
}
