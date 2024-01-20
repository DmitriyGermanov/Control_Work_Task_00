import os


class FileHandler:
    def __init__(self, filename):
        self.file_path = os.path.dirname(os.path.realpath(__file__)) + "\\data\\" + filename

    def read_file(self):
        flag = True
        while flag:
            try:
                with open(self.file_path, "r") as f:
                    flag = False
                    return f.read()
            except FileNotFoundError:
                try:
                    with open(self.file_path, "w") as f:
                        f.write("")
                except FileNotFoundError:
                    pass

    def write_file(self, content):
        try:
            with open(self.file_path, "w") as f:
                f.write(content)
        except FileNotFoundError:
            pass
