from view.commands.command import Command


class DeleteNote(Command):
    def __init__(self, console_ui):
        super().__init__(console_ui, "Удалить заметку по номеру")

    def execute(self):
        self.get_console_ui().delete_note_by_index()

    def get_console_ui(self):
        return super().get_console_ui()

    def get_description(self):
        return super().get_description()