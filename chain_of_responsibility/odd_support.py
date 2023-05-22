from support import Support


class OddSupport(Support):
    def __init__(self, name):
        super().__init__(name)

    def _resolve(self, trouble):
        return trouble.get_number() % 2 == 1
