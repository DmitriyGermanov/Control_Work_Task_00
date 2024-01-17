from view.commands.exit import Exit


class MainMenu:
    def __init__(self, console_ui):
        self.command_list = [Exit(console_ui)]

    def menu(self):
        for i in range(1, len(self.command_list) + 1):
            print(f"{i}. {self.command_list[i - 1].get_description()}")

    def execute(self, choice):
        self.command_list[choice - 1].execute()
