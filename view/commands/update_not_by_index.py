from view.commands.command import Command

class UpdateNoteByIndex(Command):

    def __init__(self, console_ui):
        super().__init__(console_ui, "Внести изменения в заметку по номеру")

    def execute(self):
        self.console_ui.update_note_by_index()

    def get_console_ui(self):
        return super().get_console_ui()

    def get_description(self):
        return super().get_description()