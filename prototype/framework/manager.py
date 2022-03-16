import copy


class Manager:
    def __init__(self):
        self.showcase = {}

    def register(self, name, proto):
        return self.showcase.update({name: proto})

    def create(self, protoname):
        p = self.showcase[protoname]
        return p.create_clone()
        # return copy.deepcopy(p)
