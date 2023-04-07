from display import Display
from string_display_impl import StringDisplayImpl
from count_display import CountDisplay


def main():
    d1 = Display(StringDisplayImpl("Hello, Japan."))
    d2 = CountDisplay(StringDisplayImpl("Hello, World."))
    d3 = CountDisplay(StringDisplayImpl("Hello, Universe."))
    d1.display()
    d2.display()
    d3.display()
    d3.multi_display(5)


if __name__ == "__main__":
    main()
