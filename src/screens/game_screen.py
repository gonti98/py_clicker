from textual.screen import Screen
from textual.containers import CenterMiddle
from textual.widgets import Label, Footer
from textual.reactive import reactive

from src.utils.temp_save_load import Temp

class GameScreen(Screen):
    points: reactive[int] = reactive(0)

    BINDINGS = [
        ("space", "press_space", "to get points"),
        ("escape", "press_escape", "to main menu"),
    ]

    def compose(self):
        yield CenterMiddle(Label("Press SPACE (0)", id="counter"))
        yield Footer()

    def on_mount(self) -> None:
        self.points = Temp.load()

    def watch_points(self, points: int):
        self.query_one("#counter", Label).update(f"Press SPACE ({points})")

    def action_press_space(self) -> None:
        self.points += 1

    def action_press_escape(self) -> None:
        Temp.save(self.points)
        self.app.switch_screen("Menu")
