from os import path as os_path
from dataclasses import dataclass

BACKSLASH_OS_WINDOWS = "\\"
# Текущая и основная рабочая директория
CURRENT_PATH = os_path.dirname(__file__)
MAIN_PATH = BACKSLASH_OS_WINDOWS.join(CURRENT_PATH.split(BACKSLASH_OS_WINDOWS)[:-2])
# Директория с изображениями
IMAGES_PATH = f"{MAIN_PATH}/imgs"
# Директория с базой данных
DB_PATH = f"{MAIN_PATH}/db/films.db"

# Название таблицы в хранилище (SQLite3 БД)
NAME_TABLE_FILMS = "films"
# Названия для столбцов таблицы
head_films = {
    "Название": None,
    "Кино/Сериал": ("Кино", "Сериал"),
    "Жанр": ("Комедия", "Ужасы", "Драма", "Мелодрама", "Триллер", "Приключения", "Боевик", "Фантастика"),
    "Просмотр": ("Просмотрено", "Непросмотрено"),
    "ID": None,
}


@dataclass(slots=True, frozen=True)
class SettingsApplication:
    """ Настройки окна приложения """
    title: str = "Collection of films"  # название окна приложения
    width: int = 1000  # ширина окна приложения
    height_min: int = 700  # минимальная высота окна приложения
    height_max: int = 1000  # максимальная высота окна приложения
    height_widgets: int = 50  # высота компонентов в приложении
    margin: int = 30  # внутренняя рамка для окна приложения
    max_len_field: int = 100  # максимальная длина строки в поле


@dataclass(slots=True, frozen=True)
class ImagesApplication:
    """ Различные лого и иконки для приложения и виджетов """
    icon_save = f"{IMAGES_PATH}/save.png"
    icon_add = f"{IMAGES_PATH}/add.png"
    icon_view = f"{IMAGES_PATH}/view.png"
    icon_delete = f"{IMAGES_PATH}/delete.png"
    icon_close = f"{IMAGES_PATH}/close.png"


@dataclass(slots=True)
class Query:
    """ Запросы к БД SQLite """
    CREATE_TABLE_FILMS = f"CREATE TABLE IF NOT EXISTS {NAME_TABLE_FILMS} " \
                         f"(id INTEGER PRIMARY KEY, name TEXT, movie_or_series TEXT, genre TEXT, view TEXT);"
    INSERT_FILM = f"INSERT INTO {NAME_TABLE_FILMS} (id, name, movie_or_series, genre, view) " \
                  f"VALUES (%s, '%s', '%s', '%s', '%s');"
    SELECT_ALL_FILMS = f"SELECT name, movie_or_series, genre, view, id FROM {NAME_TABLE_FILMS};"
    UPDATE_FILM = f"UPDATE {NAME_TABLE_FILMS} SET name='%s', movie_or_series='%s', genre='%s', view='%s' WHERE id=%s;"
    GET_MAX_ID = f"SELECT COUNT(*) FROM {NAME_TABLE_FILMS};"


@dataclass(slots=True, frozen=True)
class FontStyle:
    """ Список шрифтов и их размеров """
    CORBEL = "Corbel"
    SIZE_1 = 1
    SIZE_5 = 5
    SIZE_20 = 25


@dataclass(slots=True, frozen=True)
class Pallete:
    """ Цветовая палитра """
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    DARK_RED = "#D72323"
    ORANGE = "#FF9C00"
    LIGHT_GREY = "#CED6E0"
    DARK_BLUE = "#283149"
    LIGHT_BLUE = "#4C5C8A"


@dataclass(slots=True, frozen=True)
class WidgetName:
    """ Список названий виджетов приложения (и главные окна) """
    TITLE = "Collection of films"
    FORM_ADD = "Добавить запись"
    FORM_EDIT = "Редактировать запись"
    FORM_VIEW = "Просмотр данных"


settings_app = SettingsApplication()

images_app = ImagesApplication()
