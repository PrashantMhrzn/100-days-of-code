# Using Class

class OpenFile():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

# Using Function

from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    f = open(filename, mode)
    yield f
    f.close()


# with OpenFile('sample.txt','w') as f:
#     f.write('sample text 1')

# with open_file('sample2.txt', 'w') as f:
#     f.write('sample2 text')