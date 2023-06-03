#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-

from sys import argv, exit

from form_ui import Ui_Window
from services import WidgetFilm


if __name__ == "__main__":
    # Создание окна приложения
    app = Ui_Window(argv)
    # Пользовательский интерфейс и логика
    ui = WidgetFilm()
    exit(app.exec_())
