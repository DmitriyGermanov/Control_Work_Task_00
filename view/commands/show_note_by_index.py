from view.commands.command import Command


class ShowNoteByIndex(Command):
    def __init__(self, console_ui):
        super().__init__(console_ui, "Показать заметку по индексу")

    def execute(self):
        self.get_console_ui().show_note_by_index()

    def get_console_ui(self):
        return super().get_console_ui()

    def get_description(self):
        return super().get_description()