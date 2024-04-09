from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize, QRect, QTimer
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QComboBox,
                             QPushButton, QTableWidget, QTableWidgetItem, QAbstractItemView)
from src.ui import LIGHT_THEME
from src.storages import ContainerWidget
from src.config import settings_app as sapp, images_app as iapp, head_films, WidgetName as WN


class UiWindow(QApplication):
    """ Класс для создания окна приложения """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class UiWidget(QWidget):
    """ Класс общих параметров для виджетов """
    def __init__(self) -> None:
        super().__init__()
        self.setStyleSheet(LIGHT_THEME)
        self.show()


class UiMainWidget(UiWidget):
    """ Набор визуальных компонентов главного окна """
    def __init__(self) -> None:
        UiWidget.__init__(self)
        # self.Timer = QTimer()
        self.setMinimumSize(QSize(sapp.width, sapp.height_min))
        self.setMaximumSize(QSize(sapp.width, sapp.height_max))
        self.setWindowTitle(WN.TITLE)
        self.__setup_ui()

    def __setup_ui(self) -> None:
        """ Устанавливаем виджеты """
        self.table = QTableWidget(self)  # Создание таблицы
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.pbAdd = PushButton(sapp.height_widgets, sapp.height_widgets, icon=iapp.icon_add)
        self.pbDel = PushButton(sapp.height_widgets, sapp.height_widgets, icon=iapp.icon_delete)
        self.pbView = PushButton(sapp.height_widgets, sapp.height_widgets, icon=iapp.icon_view)
        self.gridlayout = QGridLayout(self)  # Разметка виджетов приложения
        self.gridlayout.addWidget(self.pbAdd, 1, 0, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.gridlayout.addWidget(self.pbDel, 1, 1, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.gridlayout.addWidget(self.pbView, 1, 2, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.gridlayout.addWidget(self.table, 0, 0, 1, 3)
        # self.lbNotification = QLabel(self)  # Лэйбл для отображения ошибок или уведомлений
        # self.lbNotification.setGeometry(QRect(5, sapp.height_min-(sapp.height_widgets*2+5), sapp.width-10, sapp.height_widgets*2))
        # self.lbNotification.setVisible(False)

    def createTable(self, head: tuple | list, data: tuple | list) -> None:
        """ Создание таблицы """
        self.table.setColumnCount(len(head))
        self.table.setHorizontalHeaderLabels(head)
        for row, rows in enumerate(data):
            self.table.setRowCount(row+1)
            self.createRow(row, rows)

    def insertRowInTable(self, row: int, data: tuple | list) -> None:
        """ Добавление одной записи в таблицу """
        self.table.setRowCount(row+1)
        self.createRow(row, data)

    def updateRowInTable(self, row: int, data: tuple | list) -> None:
        """ Обновление одной записи в таблице """
        self.createRow(row, data)

    def createRow(self, row: int, data: tuple | list) -> None:
        """ Создание одной записи в таблице """
        for column, value in enumerate(data):
            item = QTableWidgetItem(str(value))
            self.table.setItem(row, column, item)
            if column == 0:
                self.table.setColumnWidth(column, 400)
            else:
                self.table.setColumnWidth(column, 180)


class UiPopupForm(UiWidget):
    """ Набор визуальных компонентов всплывающего окна """
    def __init__(self, x: int, y: int) -> None:
        UiWidget.__init__(self)
        count_widgets: int = len(head_films.keys())
        width: int = int(sapp.width/1.3)
        height: int = (sapp.height_widgets+sapp.margin) * count_widgets
        self.__widgets: list[ContainerWidget | None] = [None] * count_widgets
        self.setGeometry(x+(int(sapp.width/2))-int(width/2), y+int(height*0.2), width, height)
        self.pbOk = PushButton(sapp.height_widgets, sapp.height_widgets, icon=iapp.icon_save)
        self.pbCancel = PushButton(sapp.height_widgets, sapp.height_widgets, icon=iapp.icon_close)
        self.gridlayout = QGridLayout(self)  # Разметка виджетов приложения

    def createWidgets(self, data: tuple | list = None) -> None:
        """ Добавление виджетов на форму """
        head = list(head_films.keys())
        lineedit = LineEdit(0, sapp.height_widgets, data[0] if data else "", head[0])
        self.gridlayout.addWidget(lineedit, 0, 0, 1, 2)
        self.__widgets[0] = ContainerWidget(obj=lineedit, tag="LineEdit")
        for index, item in enumerate(head):
            if (films := head_films.get(item)) is None:
                continue
            combobox = Combobox(0, sapp.height_widgets, films, films.index(data[index]) if data else 0)
            self.gridlayout.addWidget(combobox, index, 0, 1, 2)
            self.__widgets[index] = ContainerWidget(obj=combobox, tag="Combobox")
        self.gridlayout.addWidget(self.pbOk, index, 0, alignment=Qt.AlignLeft | Qt.AlignBottom)
        self.gridlayout.addWidget(self.pbCancel, index, 1, alignment=Qt.AlignRight | Qt.AlignBottom)

    def getDataFromAllFields(self) -> tuple | list:
        result = []
        for widget in self.__widgets:
            if widget is None:
                continue
            elif widget.tag == "LineEdit":
                result.append(widget.obj.text())
            elif widget.tag == "Combobox":
                result.append(widget.obj.currentText())
        return result


class UiFormAdd(UiPopupForm):
    """ Форма для добавления данных """
    def __init__(self, x: int, y: int) -> None:
        UiPopupForm.__init__(self, x, y)
        self.setWindowTitle(WN.FORM_ADD)
        self.createWidgets()


class UiFormEdit(UiPopupForm):
    """ Форма для редактирования данных """
    def __init__(self, x: int, y: int) -> None:
        UiPopupForm.__init__(self, x, y)
        self.setWindowTitle(WN.FORM_EDIT)


class UiFormDelete(UiPopupForm):
    """ Форма для редактирования данных """
    def __init__(self, x: int, y: int) -> None:
        UiPopupForm.__init__(self, x, y)
        self.setWindowTitle(WN.FORM_DEL)
        self.createWidgets()


class UiFormView(UiPopupForm):
    """ Форма для просмотра необходимых данных """
    def __init__(self, x: int, y: int) -> None:
        UiPopupForm.__init__(self, x, y)
        self.setWindowTitle(WN.FORM_VIEW)


class UiNotification(QLabel):
    def add(self, text: str, style: str) -> None:
        """ Устанавливаем текст/стиль/видимость уведомления """
        self.setText(text)
        self.setStyleSheet(style)
        self.setVisible(True)
        self.setup()

    def setup(self) -> None:
        self.setGeometry(QRect(5, sapp.height_min-(sapp.height_widgets*2+5), sapp.width-10, sapp.height_widgets*2))
        self.setMinimumSize(QSize(sapp.width, sapp.height_min))
        self.setMaximumSize(QSize(sapp.width, sapp.height_max))


class PushButton(QPushButton):
    def __init__(self, width: int, height: int, name: str = None, icon: str = None) -> None:
        QPushButton.__init__(self)
        self.setMinimumSize(QSize(width, height))
        if name is not None:
            self.setObjectName(name)
        if icon is not None:
            self.setIcon(QIcon(icon))


class LineEdit(QLineEdit):
    def __init__(self, width: int, height: int, text: str, placeholder: str) -> None:
        QLineEdit.__init__(self)
        self.setMinimumSize(QSize(width, height))
        self.setPlaceholderText(placeholder)
        self.setText(text)


class Combobox(QComboBox):
    def __init__(self, width: int, height: int, names: tuple | list = None, index: int = None) -> None:
        QComboBox.__init__(self)
        self.setMinimumSize(QSize(width, height))
        if names is not None:
            self.addItems(names)
            self.setCurrentIndex(index)
