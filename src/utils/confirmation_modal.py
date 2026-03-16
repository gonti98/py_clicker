from textual.containers import Grid
from textual.screen import ModalScreen
from textual.widgets import Button, Label


class ConfirmationModal(ModalScreen[bool]):
    AUTO_FOCUS = "#no"

    def __init__(self, message: str):
        super().__init__()
        self.message = message

    def compose(self) -> ComposeResult:
        yield Grid(
            Label(self.message, id="question"),
            Button("Yes", id="yes"),
            Button("No", id="no"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        result = event.button.id == "yes"
        self.dismiss(result)
