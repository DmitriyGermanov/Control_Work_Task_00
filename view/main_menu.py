from view.commands.add_note import AddNote
from view.commands.exit import Exit
from view.commands.show_all_notes import ShowAllNotes
from view.commands.show_note_by_index import ShowNoteByIndex
from view.commands.show_notes_by_date import ShowNotesByDate
from view.commands.show_notes_by_title import ShowNotesByTitle
from view.commands.update_not_by_index import UpdateNoteByIndex


class MainMenu:
    def __init__(self, console_ui):
        self.command_list = [AddNote(console_ui), ShowAllNotes(console_ui), ShowNoteByIndex(console_ui),
                             UpdateNoteByIndex(console_ui), ShowNotesByDate(console_ui),
                             ShowNotesByTitle(console_ui), Exit(console_ui)]

    def menu(self):
        menu = ""
        for i in range(1, len(self.command_list) + 1):
            menu = menu + f"{i}.{self.command_list[i - 1].get_description()}"
            if i != len(self.command_list):
                menu = menu + "\n"
        return menu

    def execute(self, choice):
        self.command_list[choice - 1].execute()
