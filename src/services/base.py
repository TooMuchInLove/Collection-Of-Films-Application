from src.ui import UiMainWidget, UiFormAdd, UiFormEdit, UiFormDelete
# from src.ui import UiNotification, S_ERROR, S_NOTIFICATION
from src.storages import SQLite3DataBase
from src.config import head_films


class WidgetFilm:
    """ Логика главного приложения """
    def __init__(self) -> None:
        self.__db = SQLite3DataBase()  # Подключение к БД
        self.__max_uuid = self.__db.get_last_id()
        self.__count_rows = self.__db.get_count_rows()
        self.__selected_row = self.__selected_data = None
        self.__app = UiMainWidget()  # Пользовательский интерфейс и компоненты
        self.__create_table()  # Заполняем таблицу данными
        # События нажатия на кнопки и пункты дерева
        self.__app.table.cellDoubleClicked.connect(self.__event_open_edit_form)
        self.__app.table.cellClicked.connect(self.__event_select_data)
        self.__app.pbAdd.clicked.connect(self.__event_open_add_form)
        self.__app.pbDel.clicked.connect(self.__event_open_del_form)
        # Запуск таймера, после установка метода .start()
        # self.__app.Timer.timeout.connect(self.__event_tick_timer)

    def __event_open_add_form(self) -> None:
        """ Событие: создаём и открываем форму для добавления записи """
        position = self.__app.pos()
        self.__form = UiFormAdd(position.x(), position.y())
        self.__form.pbOk.clicked.connect(self.__event_insert_data)
        self.__form.pbCancel.clicked.connect(self.__event_close_form)

    def __event_open_edit_form(self) -> None:
        """ Событие: создаём и открываем форму для редактирования записи """
        position = self.__app.pos()
        self.__form = UiFormEdit(position.x(), position.y())
        self.__form.createWidgets(self.__selected_data)
        self.__form.pbOk.clicked.connect(self.__event_update_data)
        self.__form.pbCancel.clicked.connect(self.__event_close_form)

    def __event_open_del_form(self) -> None:
        """ Событие: создаём и открываем форму для подтверждения удаления данных """
        if self.__selected_data is None:
            return None
        position = self.__app.pos()
        self.__form = UiFormDelete(position.x(), position.y())
        self.__form.createWidgets(self.__selected_data)
        self.__form.pbOk.clicked.connect(self.__event_delete_data)
        self.__form.pbCancel.clicked.connect(self.__event_close_form)

    def __event_insert_data(self) -> None:
        """ Событие: добавление данных """
        data = self.__form.getDataFromAllFields()
        self.__db.save(data)
        self.__app.insertRowInTable(self.__count_rows, data+[self.__max_uuid])
        self.__event_close_form()
        self.__count_rows += 1
        self.__max_uuid += 1

    def __event_update_data(self) -> None:
        """ Событие: обновление данных """
        uuid = int(self.__selected_data[-1])
        data = self.__form.getDataFromAllFields() + [uuid]
        self.__db.update(data)
        self.__app.updateRowInTable(self.__selected_row, data)
        self.__event_close_form()

    def __event_delete_data(self) -> None:
        """ Событие: удаление данных """
        self.__db.delete(self.__selected_data[-1])
        self.__create_table()
        self.__event_close_form()
        self.__count_rows -= 1
        self.__selected_data = None

    def __event_select_data(self, row: int, column: int) -> None:
        """ Событие: выбор (выделение) данных """
        self.__selected_row = row
        self.__selected_data = self.__get_select_data(row)

    def __event_close_form(self) -> None:
        """ Событие: закрытие формы """
        self.__form.close()

    def __create_table(self) -> None:
        """ Создание таблицы приложения """
        self.__app.createTable(head_films.keys(), self.__db.read())

    def __get_select_data(self, row: int) -> tuple:
        """ Получаем все значения из выбранной строки """
        return (
            self.__app.table.model().index(row, 0).data(),
            self.__app.table.model().index(row, 1).data(),
            self.__app.table.model().index(row, 2).data(),
            self.__app.table.model().index(row, 3).data(),
            self.__app.table.model().index(row, 4).data(),
        )

    # TODO: Обязательно допишу реализацию всплывающего окна уведомлений
    # def __event_tick_timer(self) -> None:
    #     """ Запуск таймера в приложении """
    #     self.__app.Timer.stop()
    #     # Убираем ошибку с экрана
    #     self.__app.lbNotification.setVisible(False)

    # def __popup_notification(self, _text: str, _style: str) -> None:
    #     """ Устанавливаем текст/стиль/видимость для уведомления о действиях """
    #     self.__app.lbNotification.setText(_text)
    #     self.__app.lbNotification.setStyleSheet(_style)
    #     self.__app.lbNotification.setVisible(True)
    #     # Запуск таймера для отображения ::label
    #     self.__app.Timer.start(1500)
