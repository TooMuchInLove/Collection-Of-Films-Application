#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-

from sys import argv, exit
from ui import UiWindow
from services import WidgetFilm


def main() -> None:
    app = UiWindow(argv)
    _ = WidgetFilm()  # var ui
    exit(app.exec_())


if __name__ == "__main__":
    main()
