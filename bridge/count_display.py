from display import Display


class CountDisplay(Display):
    def __init__(self, impl):
        super().__init__(impl)

    def multi_display(self, times):
        super().open()
        for i in range(times):
            super().print()
        super().close()
