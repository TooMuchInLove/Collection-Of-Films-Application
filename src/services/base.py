from src.ui import UiMainWidget, UiFormAdd, UiFormEdit, UiNotification
from src.storages import SQLite3DataBase, saver, reader, updater
from src.config import head_films
# from ui import S_ERROR, S_NOTIFICATION


class WidgetFilm:
    """ Логика главного приложения. """
    def __init__(self):
        self.__app = UiMainWidget()  # Пользовательский интерфейс и компоненты
        self.__db = SQLite3DataBase()  # Подключение к БД
        self.__create_table()  # Заполняем таблицу данными
        # События нажатия на кнопки и пункты дерева
        self.__app.table.cellDoubleClicked.connect(self.__event_open_update_form)
        self.__app.pbAdd.clicked.connect(self.__event_open_add_form)
        # Запуск таймера, после установка метода .start()
        # self.__app.Timer.timeout.connect(self.__event_tick_timer)

    def __event_open_add_form(self) -> None:
        """ Событие: открываем форму для добавления записи. """
        self.__form = UiFormAdd()

    def __event_open_update_form(self, row: int, column: int) -> None:
        """ Событие: открываем форму для редактирования записи. """
        self.__form = UiFormEdit()
        # count = self.__form.count_widgets
        # data = self.get_data_for_row(row, count)
        data = self.get_data_for_row(row, 0)
        # print(data)
        self.__form.addWidgetsForForm(data)
        # #
        # notification = UiNotification()
        # notification.add("test", "test")
        # События нажатия на кнопки
        # self.__form.pbOk.clicked.connect(self.__update_row)

    # def __event_tick_timer(self) -> None:
    #     """ Запуск таймера в приложении. """
    #     self.__app.Timer.stop()
    #     # Убираем ошибку с экрана
    #     self.__app.lbNotification.setVisible(False)

    # def __popup_notification(self, _text: str, _style: str) -> None:
    #     """ Устанавливаем текст/стиль/видимость для уведомления о действиях. """
    #     self.__app.lbNotification.setText(_text)
    #     self.__app.lbNotification.setStyleSheet(_style)
    #     self.__app.lbNotification.setVisible(True)
    #     # Запуск таймера для отображения ::label
    #     self.__app.Timer.start(1500)

    def __create_table(self) -> None:
        """ Создание таблицы приложения. """
        self.__app.createTable(head_films.keys(), reader(self.__db))

    def get_data_for_row(self, row: int, count: int) -> tuple:
        """ Получаем все значения из выбранной строки. """
        return (
            self.__app.table.model().index(row, 0).data(),
            self.__app.table.model().index(row, 1).data(),
            self.__app.table.model().index(row, 2).data(),
            self.__app.table.model().index(row, 3).data(),
            self.__app.table.model().index(row, 4).data(),
        )
