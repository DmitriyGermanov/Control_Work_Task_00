from view.commands.command import Command


class ShowNotesByDate(Command):
    def __init__(self, console_ui):
        super().__init__(console_ui, "Показать заметки за выбранный период")

    def execute(self):
        self.console_ui.show_notes_by_date()

    def get_console_ui(self):
        return super().get_console_ui()

    def get_description(self):
        return super().get_description()
