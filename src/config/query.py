from dataclasses import dataclass
from .base import NAME_TABLE_FILMS


@dataclass(slots=True)
class Query:
    """ Запросы к БД SQLite """
    CREATE_TABLE_FILMS = f"CREATE TABLE IF NOT EXISTS {NAME_TABLE_FILMS} (id INTEGER PRIMARY KEY AUTOINCREMENT, " \
                         f"name TEXT, type TEXT, genre TEXT, view TEXT);"
    SELECT_ALL_FILMS = f"SELECT name, type, genre, view, id FROM {NAME_TABLE_FILMS};"
    SELECT_FILM_NAMES = f"SELECT name FROM {NAME_TABLE_FILMS};"
    INSERT_FILM = f"INSERT INTO {NAME_TABLE_FILMS} (name, type, genre, view) " \
                  f"VALUES ('%s', '%s', '%s', '%s');"
    UPDATE_FILM = f"UPDATE {NAME_TABLE_FILMS} SET name='%s', type='%s', genre='%s', view='%s' WHERE id=%s;"
    DELETE_FILM = f"DELETE FROM {NAME_TABLE_FILMS} WHERE id=%s;"
    GET_COUNT_ROWS = f"SELECT COUNT(*) FROM {NAME_TABLE_FILMS};"
    GET_MAX_ID = f"SELECT MAX(id) FROM {NAME_TABLE_FILMS};"
