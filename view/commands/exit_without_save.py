from view.commands.command import Command


class ExitWithoutSave(Command):

    def __init__(self, console_ui):
        super().__init__(console_ui, "Завершить работу без сохранения")

    def get_console_ui(self):
        return super().get_console_ui()

    def execute(self):
        self.get_console_ui().set_work(False, False)

    def get_description(self):
        return super().get_description()
