from textual.app import App, ComposeResult
from textual.widgets import Header, Button, Static, Footer
from textual.containers import Horizontal, Container

class ContactBookApp(App):

    TITLE = "RP Contacts"
    SUB_TITLE = "A Contacts Book App with Textual and Python"
    BINDINGS = [('m', 'Taggle Dark', 'Toggle Dark Mode')]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Button('exit', id='exit_button', variant='error')

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'exit_button':
            self.exit()

    def action_toggle_dark(self):
            self.dark = not self.dark

if __name__ == "__main__":
    app = ContactBookApp()
    app.run()
