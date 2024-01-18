class Note:
    def __init__(self):
        self.note_content = None
        self.title = None

    def get_title(self):
        return self.title

    def get_note_content(self):
        return self.note_content

    def set_title(self, title):
        self.title = title

    def set_note_content(self, note_content):
        self.note_content = note_content

    def __str__(self):
        return "Заголовок заметки: " + self.title + "\nСодержание заметки: " + self.note_content
