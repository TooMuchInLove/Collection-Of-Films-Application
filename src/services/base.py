from src.ui import UiMainWidget, UiFormAdd, UiFormEdit
# from src.ui import UiNotification, S_ERROR, S_NOTIFICATION
from src.storages import SQLite3DataBase, saver, reader, updater
from src.config import head_films


class WidgetFilm:
    """ Логика главного приложения """
    def __init__(self) -> None:
        self.__db = SQLite3DataBase()  # Подключение к БД
        self.__max_uuid = self.__db.get_id()
        self.__app = UiMainWidget()  # Пользовательский интерфейс и компоненты
        self.__create_table()  # Заполняем таблицу данными
        # События нажатия на кнопки и пункты дерева
        self.__app.table.cellDoubleClicked.connect(self.__event_open_edit_form)
        self.__app.pbAdd.clicked.connect(self.__event_open_add_form)
        # Запуск таймера, после установка метода .start()
        # self.__app.Timer.timeout.connect(self.__event_tick_timer)

    def __event_open_add_form(self) -> None:
        """ Событие: создаём и открываем форму для добавления записи """
        self.__form = UiFormAdd()
        self.__form.pbOk.clicked.connect(self.__event_insert_data)
        self.__form.pbCancel.clicked.connect(self.__event_close_form)

    def __event_open_edit_form(self, row: int, column: int) -> None:
        """ Событие: создаём и открываем форму для редактирования записи """
        self.__row = row
        self.__form = UiFormEdit()
        self.__form.createWidgets(self.__get_select_data(self.__row, 0))
        self.__form.pbOk.clicked.connect(self.__event_update_data)
        self.__form.pbCancel.clicked.connect(self.__event_close_form)

    def __event_insert_data(self) -> None:
        """ Событие: добавление данных """
        data = self.__form.getDataAllFields()
        saver([self.__max_uuid]+data, self.__db)
        self.__app.insertRowInTable(self.__max_uuid-1, data+[self.__max_uuid])
        self.__event_close_form()

    def __event_update_data(self) -> None:
        """ Событие: обновление данных """
        data = self.__form.getDataAllFields() + [self.__row+1]
        updater(data, self.__db)
        self.__app.updateRowInTable(self.__row, data)
        self.__event_close_form()

    def __event_close_form(self) -> None:
        """ Событие: закрытие формы """
        self.__form.close()

    def __create_table(self) -> None:
        """ Создание таблицы приложения """
        self.__app.createTable(head_films.keys(), reader(self.__db))

    def __get_select_data(self, row: int, count: int) -> tuple:
        """ Получаем все значения из выбранной строки """
        return (
            self.__app.table.model().index(row, 0).data(),
            self.__app.table.model().index(row, 1).data(),
            self.__app.table.model().index(row, 2).data(),
            self.__app.table.model().index(row, 3).data(),
            self.__app.table.model().index(row, 4).data(),
        )

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
