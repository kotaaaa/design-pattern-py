from entry import Entry


class File(Entry):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def _print_list(self, prefix):
        print(prefix + "/" + self.to_string())
