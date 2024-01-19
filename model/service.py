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

    def update_note(self, index, title, text):
        self.note_book.update_note(index, title, text)
        return True

    def show_notes_by_date(self, start_date, end_date):
        note_by_date_list = self.note_book.get_notes_by_date(start_date, end_date)
        string_notes_list = ""
        for i in range(len(note_by_date_list)):
            string_notes_list = string_notes_list + f"{i + 1}. {note_by_date_list[i].__str__()} \n"
        return string_notes_list
