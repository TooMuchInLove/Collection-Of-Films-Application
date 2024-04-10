from src.ui import UiMainWidget, UiFormAdd, UiFormEdit, UiFormDelete
# from src.ui import UiNotification, S_ERROR, S_NOTIFICATION
from src.storages import SQLite3DataBase
from src.config import Query as Q, head_films


class WidgetFilm:
    """ Логика главного приложения """

    def __init__(self) -> None:
        self.__db = SQLite3DataBase()
        self.__max_uuid = self.__db.get_last_id()
        self.__count_rows = self.__db.get_count_rows()
        self.__selected_row = self.__selected_data = None
        self.__app = UiMainWidget()
        self.__create_table()
        self.__app.table.cellDoubleClicked.connect(self.__event_open_edit_form)
        self.__app.table.cellClicked.connect(self.__event_select_data)
        self.__app.pbAdd.clicked.connect(self.__event_open_add_form)
        self.__app.pbDel.clicked.connect(self.__event_open_del_form)
        # self.__app.Timer.timeout.connect(self.__event_tick_timer)

    def __event_open_add_form(self) -> None:
        """ Событие: создаём и открываем форму для добавления записи """
        self.__form = UiFormAdd(*self.get_position_app())
        self.__form.pbOk.clicked.connect(self.__event_insert_data)
        self.__form.pbCancel.clicked.connect(self.__event_close_form)

    def __event_open_edit_form(self) -> None:
        """ Событие: создаём и открываем форму для редактирования записи """
        self.__form = UiFormEdit(*self.get_position_app())
        self.__form.createWidgets(self.__selected_data)
        self.__form.pbOk.clicked.connect(self.__event_update_data)
        self.__form.pbCancel.clicked.connect(self.__event_close_form)

    def __event_open_del_form(self) -> None:
        """ Событие: создаём и открываем форму для подтверждения удаления данных """
        if self.__selected_data is None:
            return None
        self.__form = UiFormDelete(*self.get_position_app())
        self.__form.createWidgets(self.__selected_data)
        self.__form.pbOk.clicked.connect(self.__event_delete_data)
        self.__form.pbCancel.clicked.connect(self.__event_close_form)

    def __event_insert_data(self) -> None:
        """ Событие: добавление данных """
        data = self.__form.getDataFromAllFields()
        if self.is_check_film(data[0]):
            # TODO: заглушка! исправлю, когда доделаю систему уведомлений.
            print("Такой фильм уже существует в базе.")
            return None
        self.__db.save(Q.INSERT_FILM % (*data,))
        self.__app.insertRowInTable(self.__count_rows, data+[self.__max_uuid])
        self.__event_close_form()
        self.__count_rows += 1
        self.__max_uuid += 1

    def __event_update_data(self) -> None:
        """ Событие: обновление данных """
        uuid = int(self.__selected_data[-1])
        data = self.__form.getDataFromAllFields() + [uuid]
        self.__db.update(Q.UPDATE_FILM % (*data,))
        self.__app.updateRowInTable(self.__selected_row, data)
        self.__event_close_form()

    def __event_delete_data(self) -> None:
        """ Событие: удаление данных """
        self.__db.delete(Q.DELETE_FILM % (self.__selected_data[-1],))
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
        self.__app.createTable(head_films.keys(), self.__db.read(Q.SELECT_ALL_FILMS))

    def __get_select_data(self, row: int) -> tuple:
        """ Получаем все значения из выбранной строки """
        return (
            self.__app.table.model().index(row, 0).data(),
            self.__app.table.model().index(row, 1).data(),
            self.__app.table.model().index(row, 2).data(),
            self.__app.table.model().index(row, 3).data(),
            self.__app.table.model().index(row, 4).data(),
        )

    def get_position_app(self) -> tuple[int, int]:
        """ Получаем текущие координаты приложения """
        position = self.__app.pos()
        return position.x(), position.y()

    def is_check_film(self, film_from_field: str) -> bool:
        """ Проверка на то, существует ли запись с названием фильма в базе """
        films = self.__db.read(Q.SELECT_FILM_NAMES)
        for index, film in enumerate(films, 1):
            if film_from_field == film[0]:
                # TODO: лог для отладки
                # print(f"{index}: {film[0]} (data: {film_from_field})")
                return True
        return False

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
