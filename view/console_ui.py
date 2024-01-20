import os
from datetime import date

from presenter.presenter import Presenter
from view.main_menu import MainMenu


class ConsoleUI:
    def __init__(self):
        self.work = True
        self.presenter = Presenter(self)
        self.menu = MainMenu(self)

    def print_menu(self):
        print(self.menu.menu())

    def set_work(self, work, save):
        if save:
            self.presenter.write_notes_to_file()
        self.work = work

    def start(self):
        if not self.presenter.read_notes_from_file():
            print("Ошибка! Создайте папку data в основном каталоге!")
            self.set_work(False, False)
            os.system("pause")
        else:
            print("Здравствуйте, введите в консоль пункт меню и нажмите Enter")
            while self.work:
                self.print_menu()
                self.execute()

    def execute(self):
        try:
            self.menu.execute(int(input()))
        except ValueError:
            print("Ошибка! Введите число от 1 до " + str(len(self.menu.command_list)) + "\n")

    def add_note(self):
        print("Пожалуйста, введите заголовок новой заметки:")
        title = input()
        print("Пожалуйста, введите текст новой заметки:")
        text = input()
        if self.presenter.add_note(title, text):
            print("Заметка успешно добавлена\n")
        else:
            print("Ошибка. Заметка не добавлена\n")

    def show_all_notes(self):
        if not self.presenter.show_all_notes():
            print("Заметки отсутствуют")
        else:
            for i in range(len(self.presenter.show_all_notes())):
                note = self.presenter.show_all_notes()[i]
                print(f"{i + 1}. {note.get_title()}")
        print()

    def show_note_by_index(self):
        flag = True
        if len(self.presenter.show_all_notes()) == 0:
            print("Заметки отсутствуют\n")
        else:
            while flag:
                try:
                    note = self.presenter.show_note_by_index(int(input(f"Введите номер заметки: от 1 до "
                                                                       f"{len(self.presenter.show_all_notes())}\n")) - 1)
                    flag = False
                    print(f"{note.__str__()}\n")
                except ValueError:
                    print(f"Ошибка! Ввод должен быть числом\n")

    def update_note_by_index(self):
        if len(self.presenter.show_all_notes()) == 0:
            print("Заметки отсутствуют\n")
        else:
            flag = True
            while flag:
                try:
                    index = int(input(f"Введите номер заметки: от 1 до "
                                      f"{len(self.presenter.show_all_notes())}\n")) - 1
                    print("Введите заголовок заметки:")
                    title = input()
                    print("Введите текст заметки:")
                    text = input()
                    if self.presenter.update_note(index, title, text):
                        print("Заметка успешно обновлена\n")
                        flag = False
                    else:
                        print("Ошибка. Заметка не обновлена\n")
                except ValueError:
                    print(f"Ошибка! Ввод должен быть числом\n")

    def show_notes_by_date(self):
        flag = True
        while flag:
            try:
                start_date = date.fromisoformat(input("Введите начальную дату в "
                                                      "формате YYYY-MM-DD: "))
                end_date = date.fromisoformat(input("Введите конечную дату в "
                                                    "формате YYYY-MM-DD: "))
                notes_string = self.presenter.show_notes_by_date(start_date, end_date)
                if notes_string == "":
                    print("Заметки не найдены\n")
                else:
                    print(f"Список заметок в интервале: {start_date.__str__()} до {end_date.__str__()}\n")
                    print(notes_string)
                flag = False
            except ValueError:
                print(f"Ошибка! Ввод должен быть датой\n")

    def show_notes_by_title(self):
        print("Введите заголовок заметки:")
        title = input()
        notes_string = self.presenter.get_notes_by_title(title)
        if notes_string == "":
            print("Заметки не найдены\n")
        else:
            print(f"Список заметок по заголовку: {title}\n")
            print(notes_string)

    def delete_note_by_index(self):
        if len(self.presenter.show_all_notes()) == 0:
            print("Заметки отсутствуют\n")
        else:
            flag = True
            while flag:
                try:
                    index = int(input(f"Введите номер заметки: от 1 до "
                                      f"{len(self.presenter.show_all_notes())}\n")) - 1
                    if self.presenter.delete_note(index):
                        print("Заметка успешно удалена\n")
                    else:
                        print("Ошибка. Заметка не удалена\n")
                    flag = False
                except ValueError:
                    print(f"Ошибка! Ввод должен быть числом\n")