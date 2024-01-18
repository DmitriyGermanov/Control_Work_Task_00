from model.service import Service


class Presenter:

    def __init__(self, ui):
        self.ui = ui
        self.service = Service()

    def start(self):
        pass

    def start(self):
        self.ui.start()

    def add_note(self, title, text):
        self.service.add_note(title, text)
