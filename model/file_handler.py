import os


class FileHandler:
    def __init__(self, filename):
        self.file_path = os.path.dirname(os.path.realpath(__file__)) + "\\data\\" + filename

    def read_file(self):
        with open(self.file_path, "r") as f:
            return f.read()

    def write_file(self, content):
        with open(self.file_path, "w") as f:
            f.write(content)
