from model.note_book import NoteBook


class Service:
    def __init__(self):
        self.note_book = NoteBook()

    def add_note(self, title, content):
        self.note_book.add_note(title, content)
