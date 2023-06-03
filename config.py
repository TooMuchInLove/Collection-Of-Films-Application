# -*- coding: utf-8 -*-

from enum import Enum

# Ширина приложения
WIDTH = 700
# Высота приложения / минимальная
HEIGHT_MIN = 500
# Высота приложения / максимальная
HEIGHT_MAX = 500
# Высота компонентов приложения
HEIGHT_WIDGETS = 30
# Максимальная длина строки в поле
MAX_LEN_FIELD = 100
# Задержка для всплывающего сообщения
TIMEOUT = 1500
# Кодирование
ENCODING_UTF8 = "utf-8"
# Хранилище изображений
IMG_DIR = "imgs/"

# Название БД (SQLite3 БД)
PATH_DB_SQLITE_FILE = "db/films.db"
# Название таблицы в хранилище (SQLite3 БД)
NAME_TABLE_FILMS = "films"
# Названия для столбцов таблицы
head_films = {
    "ID": None,
    "Название": None,
    "Кино/Сериал": ("Кино", "Сериал"),
    "Жанр": ("Комедия", "Ужасы", "Драма", "Мелодрама","Триллер",
             "Приключения", "Боевик", "Фантастика"),
    "Просмотр": ("Просмотрено", "Непросмотрено"),
}


class Icon(Enum):
    """ Изображения .png для виджетов """
    # ICON_BACK = f"{IMG_DIR}back.png"
    # ICON_UPDATE = f"{IMG_DIR}update.png"
    # ICON_SEARCH = f"{IMG_DIR}search.png"
    ICON_SAVE = f"{IMG_DIR}save.png"
    ICON_ADD = f"{IMG_DIR}add.png"
    ICON_VIEW = f"{IMG_DIR}view.png"
    ICON_DELETE = f"{IMG_DIR}delete.png"
    ICON_CLOSE = f"{IMG_DIR}close.png"


class FontStyle(Enum):
    """ Список шрифтов и их размеров """
    CORBEL = "Corbel"
    SIZE_1 = 1
    SIZE_5 = 5
    # SIZE_10 = 10
    # SIZE_13 = 13
    SIZE_15 = 15
    # SIZE_20 = 20
    # SIZE_30 = 30
    # SIZE_40 = 40


class Pallete(Enum):
    """ Цветовая палитра """
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    DARK_RED = "#D72323"
    ORANGE = "#FF9C00"
    # DARK_GREY_1 = "#232323"
    # DARK_GREY_2 = "#2A2A2A"
    LIGHT_GREY = "#CED6E0"
    DARK_BLUE = "#283149"
    LIGHT_BLUE = "#4C5C8A"


class Notification(Enum):
    """ Список уведомлений для ::QLabel """
    EMPTY = "Поле пустое"


class WidgetName(Enum):
    """ Список названий виджетов приложения (и главные окна) """
    TITLE = "Collection of films"
    FORM_ADD = "Добавить запись"
    FORM_EDIT = "Редактировать запись"
    FORM_VIEW = "Просмотр данных"
