from textual.screen import ModalScreen
from textual.widgets import Button, Label
from textual.containers import Grid

class ConfirmationModal(ModalScreen[bool]):
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
