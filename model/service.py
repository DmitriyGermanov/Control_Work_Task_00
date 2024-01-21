from model.file_handler import FileHandler
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

    def get_notes_by_title(self, title):
        string_notes_list = ""
        notes_by_title_list = self.note_book.get_note_by_title(title)
        for i in range(len(notes_by_title_list)):
            string_notes_list = string_notes_list + f"{i + 1}. {notes_by_title_list[i].__str__()} \n"
        return string_notes_list

    def delete_note(self, index):
        return self.note_book.delete_note(index)

    def write_notes_to_file(self):
        string_notes_list = ""
        note_list = self.note_book.get_all_notes()
        for i in range(len(note_list)):
            string_notes_list = (string_notes_list + note_list[i].get_title() + ";" +
                                 note_list[i].get_note_content() + ";" +
                                 note_list[i].get_creation_date().__str__() + "\n")
        filehandler = FileHandler("notes.json")
        filehandler.write_file(string_notes_list)
        return True

    def read_notes_from_file(self):
        filehandler = FileHandler("notes.json")
        string_notes_list = filehandler.read_file()
        if string_notes_list is None:
            return False
        else:
            note_list = string_notes_list.split("\n")
            for i in range(len(note_list)):
                note_list[i] = note_list[i].split(";")
                if note_list[i][0] != "":
                    self.note_book.add_note_with_date(note_list[i][0], note_list[i][1], note_list[i][2])
            return True
