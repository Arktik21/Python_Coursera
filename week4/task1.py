import os.path
import tempfile


class File:
    def __init__(self, path):
        self.path = path
        self.curr = 0

        if not os.path.exists(path):
            with open(self.path, 'w'):
                pass

    def __str__(self):
        return self.path

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, 'r', encoding='utf8') as f:
            f.seek(self.curr)
            line = f.readline()
            if line:
                self.curr = f.tell()
                return line
            else:
                self._curr = 0
                raise StopIteration

    def __add__(self, other):
        result_path = os.path.join(tempfile.gettempdir(), 'tmp.txt')
        result = File(result_path)
        result.write(self.read() + other.read())
        return result

    def read(self):
        with open(self.path, 'r', encoding='utf8') as f:
            return f.read()

    def write(self, text):
        with open(self.path, 'w', encoding='utf8') as f:
            f.write(text)
