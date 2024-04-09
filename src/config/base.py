from os import path as os_path

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
    "Кино/Сериал": ("Кино", "Сериал", "Мультфильм", "Мультсериал"),
    "Жанр": ("Комедия", "Ужасы", "Драма", "Мелодрама", "Триллер", "Приключения", "Боевик", "Фантастика"),
    "Просмотр": ("Просмотрено", "Непросмотрено"),
    "ID": None,
}
