# -*- coding: utf-8 -*-

from sqlite3 import connect as sql_connect
from sqlite3 import Error as SQLiteError

from sing import Singleton
from config import PATH_DB_SQLITE_FILE
from config import NAME_TABLE_FILMS
from typehinting import ListData


class IStorage:
    """ Интерфейс для любого хранилища """
    def save(self, _data: ListData) -> None:
        pass

    def read(self) -> ListData:
        pass

    def update(self, _data: ListData) -> None:
        pass

    def delete(self) -> None:
        pass


class IStorageSQL(IStorage):
    """ Интерфейс для БД, хранящих данные в таблице (SQL) """
    def create_table(self) -> None:
        pass


class SQLite3DataBase(IStorageSQL, Singleton):
    """ Хранилище данных в табличном формате -> база SQLite3 """
    def __init__(self):
        # Подключение к базе
        self.connection()
        # Создание таблиц
        self.create_table()

    def connection(self) -> None:
        """ Подключение к базе """
        try:
            self.__connect = sql_connect(PATH_DB_SQLITE_FILE)
            # Создание курсора для запросов в базу
            self.__cursor = self.__connect.cursor()
        except SQLiteError as error:
            print(error)

    def create_table(self) -> None:
        """ Создание таблиц """
        self.__cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {NAME_TABLE_FILMS} (
                id INTEGER PRIMARY KEY,
                name TEXT,
                movie_or_series TEXT,
                genre TEXT,
                view TEXT
            );
        """)
        # Сохранение изменений
        self.__connect.commit()

    def save(self, _data: ListData) -> None:
        """ Сохранение данных в БД """
        self.__cursor.execute(f"""
            INSERT INTO {NAME_TABLE_FILMS} (id, name, movie_or_series, genre, view)
            VALUES (?, ?, ?, ?, ?)
        """, (_data))
        self.__connect.commit()

    def read(self) -> ListData:
        """ Чтение данных из БД """
        self.__cursor.execute(f"SELECT * FROM {NAME_TABLE_FILMS};")
        return [item for item in self.__cursor.fetchall()]

    def update(self, _data: ListData) -> None:
        """ Обновляем данные в БД """
        # UPDATE films SET name=?, mors=?, janr=?, flag=? WHERE id=?
        self.__cursor.execute(f"""
                UPDATE {NAME_TABLE_FILMS} (name, movie_or_series, genre, view)=
                (?, ?, ?, ?) WHERE id=?
            """, (_data[1:], _data[0]))
        self.__connect.commit()

    def __del__(self):
        """ Разрываем соединение с базой """
        self.__connect.close()


def saves(_data: ListData, _storage: IStorage) -> None:
    _storage.save(_data)


def reads(_storage: IStorage) -> ListData:
    return _storage.read()


def updates(_data: ListData, _storage: IStorage) -> None:
    _storage.update(_data)
