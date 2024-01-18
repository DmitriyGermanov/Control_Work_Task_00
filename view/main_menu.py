from view.commands.add_note import AddNote
from view.commands.exit import Exit


class MainMenu:
    def __init__(self, console_ui):
        self.command_list = [AddNote(console_ui), Exit(console_ui)]

    def menu(self):
        menu = ""
        for i in range(1, len(self.command_list) + 1):
            menu = menu + f"{i}.{self.command_list[i - 1].get_description()}"
            if i != len(self.command_list):
                menu = menu + "\n"
        return menu

    def execute(self, choice):
        self.command_list[choice - 1].execute()
