from model.note import Note


class NoteBook:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content):
        note = Note()
        note.set_title(title)
        note.set_note_content(content)
        self.notes.append(note)

    def get_note_book(self):
        return self.notes

    def delete_note(self, index):
        self.notes.pop(index)

    def update_note(self, index, title, content):
        self.notes[index].set_note_title(title)
        self.notes[index].set_note_content(content)

    def update_note_content(self, index, content):
        self.notes[index].set_note_content(content)

    def update_note_title(self, index, title):
        self.notes[index].set_note_title(title)

    def get_note_by_index(self, index):
        return self.notes[index]

    def get_note_by_title(self, title):
        for note in self.notes:
            if note.get_note_title() == title:
                return note

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
