from view.commands.command import Command


class ShowAllNotes(Command):
    def __init__(self, console_ui):
        super().__init__(console_ui, "Показать заголовки всех заметок")

    def execute(self):
        self.get_console_ui().show_all_notes()

    def get_console_ui(self):
        return super().get_console_ui()

    def get_description(self):
        return super().get_description()