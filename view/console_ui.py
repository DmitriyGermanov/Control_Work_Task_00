from presenter.presenter import Presenter
from view.main_menu import MainMenu


class ConsoleUI:
    def __init__(self):
        self.work = True
        self.presenter = Presenter(self)
        self.menu = MainMenu(self)

    def print_menu(self):
        print(self.menu.menu())

    def set_work(self, work):
        self.work = work

    def start(self):
        print("Здравствуйте, введите в консоль пункт меню и нажмите Enter")
        while self.work:
            self.print_menu()
            self.execute()

    def execute(self):
        self.menu.execute(int(input()))

    def add_note(self):
        print("Пожалуйста, введите заголовок новой заметки:")
        title = input()
        print("Пожалуйста, введите текст новой заметки:")
        text = input()
        if self.presenter.add_note(title, text):
            print("Заметка успешно добавлена\n")

    def show_all_notes(self):
        for i in range(len(self.presenter.show_all_notes())):
            note = self.presenter.show_all_notes()[i]
            print(f"{i + 1}. {note.get_title()} \n")

    def show_note_by_index(self):
        note = self.presenter.show_note_by_index(int(input(f"Введите номер заметки: от 1 до "
                                                           f"{len(self.presenter.show_all_notes())}\n")) - 1)
        print(f"{note.__str__()}\n")
