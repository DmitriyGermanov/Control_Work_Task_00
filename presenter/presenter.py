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

    def show_note_by_index(self, index):
        return self.service.show_note_by_index(index)

    def update_note(self, index, title, text):
        return self.service.update_note(index, title, text)

    def show_notes_by_date(self, start_date, end_date):
        return self.service.show_notes_by_date(start_date, end_date)
