class Command:
    def __init__(self, console_ui, description):
        self.console_ui = console_ui
        self.description = description

    def execute(self):
        pass

    def get_console_ui(self):
        return self.console_ui

    def get_description(self):
        return self.description
