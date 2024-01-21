from model.note import Note
from datetime import date


class NoteBook:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content):
        note = Note()
        note.set_title(title)
        note.set_note_content(content)
        self.notes.append(note)
        return True

    def add_note_with_date(self, title, content, creation_date):
        note = Note()
        note.set_title(title)
        note.set_note_content(content)
        note.set_creation_date(date.fromisoformat(creation_date))
        self.notes.append(note)
        return True

    def get_note_book(self):
        return self.notes

    def delete_note(self, index):
        if self.notes.pop(index) is not None:
            return True
        else:
            return False

    def update_note(self, index, title, content):
        self.notes[int(index)].set_title(title)
        self.notes[int(index)].set_note_content(content)
        return True

    def update_note_content(self, index, content):
        self.notes[index].set_note_content(content)

    def update_note_title(self, index, title):
        self.notes[index].set_note_title(title)

    def get_note_by_index(self, index):
        return self.notes[index]

    def get_note_by_title(self, title):
        search_notes = []
        for note in self.notes:
            if note.get_title() == title:
                search_notes.append(note)
        return search_notes

    def get_note_by_content(self, content):
        for note in self.notes:
            if note.get_note_content() == content:
                return note

    def get_note_by_title_and_content(self, title, content):
        for note in self.notes:
            if note.get_note_title() == title and note.get_note_content() == content:
                return note

    def get_all_notes(self):
        return self.notes

    def get_note_count(self):
        return len(self.notes)

    def delete_all_notes(self):
        self.notes = []

    def get_notes_by_date(self, start_date, end_date):
        notes = []
        for i in range(0, len(self.notes)):
            print(self.notes[i].get_creation_date())
            if start_date <= self.notes[i].get_creation_date() <= end_date:
                notes.append(self.notes[i])
        return notes
