from model.note_book import NoteBook


class Service:
    def __init__(self):
        self.note_book = NoteBook()

    def add_note(self, title, content):
        return self.note_book.add_note(title, content)

    def show_all_notes(self):
        return self.note_book.get_all_notes()

    def show_note_by_index(self, index):
        return self.note_book.get_note_by_index(index)
