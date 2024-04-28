"""To-Do entry point script."""

from todo_tk import gui_tk, __app_name__


def main():
    gui_tk.app(prog_name=__app_name__)


if __name__ == "__main__":
    main()