from sqlite3 import connect as sql_connect, Error as SQLiteError
from src.config import Query as Q, DB_PATH
from src.patterns import Singleton


class IStorage:
    """ Интерфейс для любого хранилища """

    def save(self, query: str) -> None:
        pass

    def read(self, query: str) -> tuple | list:
        pass

    def update(self, query: str) -> None:
        pass

    def delete(self, query: str) -> None:
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
        self.connection = self.cursor = None
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

    def get_count_rows(self) -> int:
        """ Получение кол-ва записей в таблице """
        self.cursor.execute(Q.GET_COUNT_ROWS)
        if (count := self.cursor.fetchone()[0]) is None:
            return 0
        return count

    def get_last_id(self) -> int:
        """ Получение максимального ID записи в таблице """
        self.cursor.execute(Q.GET_MAX_ID)
        if (uuid := self.cursor.fetchone()[0]) is None:
            return 1
        return uuid + 1

    def save(self, query: str) -> None:
        """ Сохранение данных в БД """
        self.cursor.execute(query)
        self.connection.commit()

    def read(self, query: str) -> tuple | list:
        """ Чтение данных из БД """
        self.cursor.execute(query)
        return [item for item in self.cursor.fetchall()]

    def update(self, query: str) -> None:
        """ Обновляем данные в БД """
        self.cursor.execute(query)
        self.connection.commit()

    def delete(self, query: str) -> None:
        """ Удаление данных из БД """
        self.cursor.execute(query)
        self.connection.commit()

    def __del__(self) -> None:
        """ Разрываем соединение с базой """
        if self.connection is not None:
            self.connection.close()
