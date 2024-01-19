from model.service import Service


class Presenter:

    def __init__(self, ui):
        self.ui = ui
        self.service = Service()

    def start(self):
        self.ui.start()

    def add_note(self, title, text):
        return self.service.add_note(title, text)

    def show_all_notes(self):
        return self.service.show_all_notes()
