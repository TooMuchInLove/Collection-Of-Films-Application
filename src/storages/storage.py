from sqlite3 import connect as sql_connect, Error as SQLiteError
from src.config import Query as Q, DB_PATH
from src.patterns import Singleton


class IStorage:
    """ Интерфейс для любого хранилища """
    def save(self, data: list) -> None:
        pass

    def read(self) -> list:
        pass

    def update(self, data: list) -> None:
        pass

    def delete(self) -> None:
        pass


class IStorageSQL(IStorage):
    """ Интерфейс для БД, хранящих данные в таблице (SQL) """
    def connect(self) -> None:
        pass

    def create_table(self) -> None:
        pass


class SQLite3DataBase(IStorageSQL, Singleton):
    """ Хранилище данных в табличном формате -> база SQLite3 """
    def __init__(self) -> None:
        self.connection = None
        self.cursor = None
        self.connect()
        self.create_table()

    def connect(self) -> None:
        """ Подключение к базе. """
        try:
            self.connection = sql_connect(DB_PATH)
            self.cursor = self.connection.cursor()
        except SQLiteError as error:
            print(error)

    def create_table(self) -> None:
        """ Создание таблицы. """
        self.cursor.execute(Q.CREATE_TABLE_FILMS)
        self.connection.commit()

    def save(self, data: list) -> None:
        """ Сохранение данных в БД. """
        self.cursor.execute(Q.INSERT_FILM, (data,))
        self.connection.commit()

    def read(self) -> list:
        """ Чтение данных из БД. """
        self.cursor.execute(Q.SELECT_ALL_FILMS)
        return [item for item in self.cursor.fetchall()]

    def update(self, data: list) -> None:
        """ Обновляем данные в БД. """
        # UPDATE films SET name=?, mors=?, janr=?, flag=? WHERE id=?
        self.cursor.execute(Q.UPDATE_FILM, (data[1:], data[0],))
        self.connection.commit()

    def __del__(self) -> None:
        """ Разрываем соединение с базой """
        if self.connection is not None:
            self.connection.close()


def saver(data: list, storage: IStorage) -> None:
    storage.save(data)


def reader(storage: IStorage) -> list:
    return storage.read()


def updater(data: list, storage: IStorage) -> None:
    storage.update(data)
