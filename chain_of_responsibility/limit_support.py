from support import Support


class LimitSupport(Support):
    def __init__(self, name, limit):
        super().__init__(caption)
        self.limit = limit

    def resolve(self, trouble):
        if trouble.get_number() < limit:
            return True
        else:
            return False
