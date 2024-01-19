import datetime


class Note:
    def __init__(self):
        self.note_content = None
        self.title = None
        self.creation_date = datetime.date.today()

    def get_title(self):
        return self.title

    def get_note_content(self):
        return self.note_content

    def get_creation_date(self):
        return self.creation_date

    def set_title(self, title):
        self.title = title

    def set_note_content(self, note_content):
        self.note_content = note_content

    def __str__(self):
        return ("Заголовок заметки: " + self.title + "\nСодержание заметки: " + self.note_content + ("\nДата создания "
                                                                                                     "заметки: ") +
                self.get_creation_date().__str__())
