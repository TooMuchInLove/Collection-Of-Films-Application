from sqlite3 import connect as sql_connect, Error as SQLiteError
from src.config import Query as Q, DB_PATH
from src.patterns import Singleton


class IStorage:
    """ Интерфейс для любого хранилища """
    def save(self, data: tuple | list) -> None:
        pass

    def read(self) -> tuple | list:
        pass

    def update(self, data: tuple | list) -> None:
        pass

    def delete(self, _id: int) -> None:
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
        """ Подключение к базе """
        try:
            self.connection = sql_connect(DB_PATH)
            self.cursor = self.connection.cursor()
        except SQLiteError as error:
            print(error)

    def create_table(self) -> None:
        """ Создание таблицы """
        self.cursor.execute(Q.CREATE_TABLE_FILMS)
        self.connection.commit()

    def get_id(self) -> int:
        """ Получение максимального ID записи в таблице """
        self.cursor.execute(Q.GET_MAX_ID)
        uuid = self.cursor.fetchone()
        if uuid is None:
            return 1
        return uuid[0] + 1

    def save(self, data: tuple | list) -> None:
        """ Сохранение данных в БД """
        self.cursor.execute(Q.INSERT_FILM % (*data,))
        self.connection.commit()

    def read(self) -> tuple | list:
        """ Чтение данных из БД """
        self.cursor.execute(Q.SELECT_ALL_FILMS)
        return [item for item in self.cursor.fetchall()]

    def update(self, data: tuple | list) -> None:
        """ Обновляем данные в БД """
        self.cursor.execute(Q.UPDATE_FILM % (*data,))
        self.connection.commit()

    def delete(self, _id: int) -> None:
        """ Удаление данных из БД """
        self.cursor.execute(Q.DELETE_FILM % (_id,))
        self.connection.commit()

    def __del__(self) -> None:
        """ Разрываем соединение с базой """
        if self.connection is not None:
            self.connection.close()
