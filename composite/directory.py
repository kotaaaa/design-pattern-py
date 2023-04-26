class Directory(Entry):
    directory = []

    def __init__(self):
        self.name = name

    def get_name(self):
        return self.name

    def get_size(self):
        size = 0
        for entry in self.directory:
            size += entry.get_size()
        return size

    def add(self, entry):
        self.directory.append(entry)

    def _print_list(self, prefix):
        print("prefix" + "/" + self.name)
        for entry in self.directory:
            entry._print_list(prefix + "/" + self.name)
