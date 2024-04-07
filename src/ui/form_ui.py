from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize, QRect, QTimer
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QComboBox,
                             QPushButton, QTableWidget, QTableWidgetItem, QAbstractItemView)
from src.ui import LIGHT_THEME
from src.config import (settings_app as sapp, images_app as iapp,
                        head_films, WidgetName as WN)


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
        super().__init__()
        self.setMinimumSize(QSize(sapp.width, sapp.height_min))
        self.setMaximumSize(QSize(sapp.width, sapp.height_max))
        self.setWindowTitle(WN.TITLE)
        # self.Timer = QTimer()
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
        # self.lbNotification.setGeometry(QRect(5, sapp.height_min-(sapp.height_widgets*2+5),
        # sapp.width-10, sapp.height_widgets*2))
        # self.lbNotification.setVisible(False)

    def createTable(self, head: list, data: list) -> None:
        """ Создание таблицы """
        self.table.setColumnCount(len(head))
        self.table.setHorizontalHeaderLabels(head)
        for i, rows in enumerate(data):
            self.table.setRowCount(i+1)
            for j, value in enumerate(rows):
                item = QTableWidgetItem(str(value))
                self.table.setItem(i, j, item)
                if j == 0:
                    item.setTextAlignment(Qt.AlignRight)


class UiPopupForm(UiWidget):
    """ Набор визуальных компонентов всплывающего окна """
    def __init__(self) -> None:
        super().__init__()
        count_widgets = len(head_films.keys())
        self.setMinimumSize(QSize(int(sapp.width/1.5), (sapp.height_widgets+sapp.margin)*count_widgets))
        self.setMaximumSize(QSize(int(sapp.width/1.5), (sapp.height_widgets+sapp.margin)*count_widgets))
        self.pbOk = PushButton(sapp.height_widgets, sapp.height_widgets, icon=iapp.icon_save)
        self.pbCancel = PushButton(sapp.height_widgets, sapp.height_widgets, icon=iapp.icon_close)
        self.gridlayout = QGridLayout(self)  # Разметка виджетов приложения

    def addWidgets(self, data: tuple = None) -> None:
        """ Добавление виджетов на форму """
        head = list(head_films.keys())
        le = QLineEdit()
        le.setText(data[0] if data else "")
        le.setPlaceholderText(head[0])
        le.setMinimumSize(QSize(0, sapp.height_widgets))
        for index, item in enumerate(head):
            films = head_films.get(item)
            if films is None:
                continue
            combobox = QComboBox()
            combobox.addItems(films)
            combobox.setCurrentIndex(films.index(data[index]) if data else 0)
            combobox.setMinimumSize(QSize(0, sapp.height_widgets))
            self.gridlayout.addWidget(combobox, index, 0, 1, 2)
        self.gridlayout.addWidget(le, 0, 0, 1, 2)
        self.gridlayout.addWidget(self.pbOk, index, 0, alignment=Qt.AlignLeft | Qt.AlignBottom)
        self.gridlayout.addWidget(self.pbCancel, index, 1, alignment=Qt.AlignRight | Qt.AlignBottom)


class UiFormAdd(UiPopupForm):
    """ Форма для добавления данных """
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(WN.FORM_ADD)
        self.addWidgets()


class UiFormEdit(UiPopupForm):
    """ Форма для редактирования данных """
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(WN.FORM_EDIT)


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
