from view.commands.command import Command


class AddNote(Command):
    def __init__(self, console_ui):
        super().__init__(console_ui, "Добавить заметку")

    def get_console_ui(self):
        return super().get_console_ui()

    def get_description(self):
        return super().get_description()

    def execute(self):
        self.get_console_ui().add_note()
