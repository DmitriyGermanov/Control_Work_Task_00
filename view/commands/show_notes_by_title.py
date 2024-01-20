from view.commands.command import Command


class ShowNotesByTitle(Command):
    def __init__(self, console_ui):
        super().__init__(console_ui, "Показать заметки по заголовку")

    def execute(self):
        self.get_console_ui().show_notes_by_title()

    def get_console_ui(self):
        return super().get_console_ui()

    def get_description(self):
        return super().get_description()