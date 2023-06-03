# -*- coding: utf-8 -*-

from form_ui import Ui_MainWidget
from form_ui import Ui_FormAdd
from form_ui import Ui_FormEdit

from storage import SQLite3DataBase
# from storage import saves
from storage import reads
# from storage import updates

# from config import Notification as N
from config import TIMEOUT
from config import head_films

# from theme import S_ERROR
# from theme import S_NOTIFICATION

from typehinting import Text
from typehinting import Index
from typehinting import TupleData


class WidgetFilm:
    """ Логика главного приложения """
    def __init__(self):
        # Пользовательский интерфейс и компоненты
        self.__app = Ui_MainWidget()
        # Заполняем таблицу данными
        self.__create_table()
        # События нажатия на кнопки и пункты дерева
        self.__app.table.cellDoubleClicked.connect(self.__event_open_update_form)
        self.__app.pbAdd.clicked.connect(self.__event_open_add_form)
        # Запуск таймера, после установка метода .start()
        self.__app.Timer.timeout.connect(self.__event_tick_timer)

    def __event_open_add_form(self) -> None:
        """ Событие: открываем форму для добавления записи """
        self.__form = Ui_FormAdd()

    def __event_open_update_form(self, row: Index, column: Index) -> None:
        """ Событие: открываем форму для редактирования записи """
        self.__form = Ui_FormEdit()
        count = self.__form.count_widgets
        data = self.get_data_for_row(row, count)
        print(data)
        self.__form.addWidgetsForForm(data)
        # События нажатия на кнопки
        # self.__form.pbOk.clicked.connect(self.__update_row)

    def __event_tick_timer(self) -> None:
        """ Запуск таймера в приложении """
        self.__app.Timer.stop()
        # Убираем ошибку с экрана
        self.__app.lbNotification.setVisible(False)

    def __popup_notification(self, _text: Text, _style: Text) -> None:
        """ Устанавливаем текст/стиль/видимость для уведомления о действиях """
        self.__app.lbNotification.setText(_text)
        self.__app.lbNotification.setStyleSheet(_style)
        self.__app.lbNotification.setVisible(True)
        # Запуск таймера для отображения ::label
        self.__app.Timer.start(TIMEOUT)

    def __create_table(self):
        """ Создание таблицы приложения """
        self.__app.createTable(head_films.keys(),
                               reads(SQLite3DataBase()))

    def get_data_for_row(self, _row: Index, _count: Index) -> TupleData:
        """ Получаем все значения из выбранной строки """
        data = (
            self.__app.table.model().index(_row, 0).data(),
            self.__app.table.model().index(_row, 1).data(),
            self.__app.table.model().index(_row, 2).data(),
            self.__app.table.model().index(_row, 3).data(),
            self.__app.table.model().index(_row, 4).data(),
        )
        return data
