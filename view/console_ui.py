from view.main_menu import MainMenu


class ConsoleUI:
    def __init__(self):
        self.work = True

    def print_menu(self):
        print(MainMenu.menu(MainMenu(self)))

    def set_work(self, work):
        self.work = work

    def start(self):
        print("Здравствуйте, введите в консоль пункт меню и нажмите Enter")
        while self.work:
            self.print_menu()
            self.execute()

    def execute(self):
        MainMenu.execute(MainMenu(self), int(input()))
