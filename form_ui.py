# -*- coding: utf-8 -*-

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QAbstractItemView

from config import WidgetName as WN
from config import Icon as I
from config import WIDTH
from config import HEIGHT_MIN
from config import HEIGHT_MAX
from config import HEIGHT_WIDGETS
from config import head_films

from typehinting import TupleData
from typehinting import ListData
from theme import LIGHT_THEME


class Ui_Window(QApplication):
    """ Класс для создания окна приложения """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Ui_Widget(QWidget):
    """ Класс общих параметров для виджетов """
    def __init__(self):
        super().__init__()
        # Стиль приложения и виджетов
        self.setStyleSheet(LIGHT_THEME)
        # Отображение формы
        self.show()


class Ui_MainWidget(Ui_Widget):
    """ Набор визуальных компонентов главного окна """
    def __init__(self):
        super().__init__()
        # Размер окна
        self.setMinimumSize(QSize(WIDTH, HEIGHT_MIN))
        self.setMaximumSize(QSize(WIDTH, HEIGHT_MAX))
        # Название окна
        self.setWindowTitle(WN.TITLE.value)
        # Таймер, уделённый под сообщения
        self.Timer = QTimer()
        # Создаём таблицу
        self.table = QTableWidget(self)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Виджеты приложения
        self.pbAdd = QPushButton()
        self.pbDel = QPushButton()
        self.pbView = QPushButton()
        # Размер виджетов
        self.pbAdd.setMinimumSize(QSize(HEIGHT_WIDGETS, HEIGHT_WIDGETS))
        self.pbDel.setMinimumSize(QSize(HEIGHT_WIDGETS, HEIGHT_WIDGETS))
        self.pbView.setMinimumSize(QSize(HEIGHT_WIDGETS, HEIGHT_WIDGETS))
        # Разметка виджетов приложения
        self.gridlayout = QGridLayout(self)
        self.gridlayout.addWidget(self.pbAdd, 1, 0, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.gridlayout.addWidget(self.pbDel, 1, 1, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.gridlayout.addWidget(self.pbView, 1, 2, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.gridlayout.addWidget(self.table, 2, 0, 1, 3)
        # Лэйбл для отображения ошибок или уведомлений
        self.lbNotification = QLabel(self)
        self.lbNotification.setGeometry(QRect(5, HEIGHT_MIN-(HEIGHT_WIDGETS*2+5), WIDTH-10, HEIGHT_WIDGETS*2))
        self.lbNotification.setVisible(False)
        self.setupIcon()

    def setupIcon(self) -> None:
        """ Устанавливаем icon для кнопок """
        self.pbAdd.setIcon(QIcon(I.ICON_ADD.value))
        self.pbDel.setIcon(QIcon(I.ICON_DELETE.value))
        self.pbView.setIcon(QIcon(I.ICON_VIEW.value))

    def createTable(self, _head: ListData, _data: ListData) -> None:
        """ Создание таблицы """
        self.table.setColumnCount(len(_head))
        self.table.setHorizontalHeaderLabels(_head)
        for i, rows in enumerate(_data):
            self.table.setRowCount(i+1)
            for j, value in enumerate(rows):
                item = QTableWidgetItem(str(value))
                self.table.setItem(i, j, item)
                if j == 0:
                    item.setTextAlignment(Qt.AlignRight)


class Ui_PopupForm(Ui_Widget):
    """ Набор визуальных компонентов всплывающего окна """
    def __init__(self):
        super().__init__()
        # Количество виджетов с данными и расстояние между ними
        self.count_widgets = len(head_films.keys())
        self.margin = 20
        # Виджеты приложения
        self.pbOk = QPushButton()
        self.pbCancel = QPushButton()
        self.gridlayout = QGridLayout(self)
        # Размер виджетов
        self.pbOk.setMinimumSize(QSize(HEIGHT_WIDGETS, HEIGHT_WIDGETS))
        self.pbCancel.setMinimumSize(QSize(HEIGHT_WIDGETS, HEIGHT_WIDGETS))
        self.setupIcon()

    def setupIcon(self) -> None:
        """ Устанавливаем icon для кнопок """
        self.pbOk.setIcon(QIcon(I.ICON_SAVE.value))
        self.pbCancel.setIcon(QIcon(I.ICON_CLOSE.value))

    def addWidgetsForForm(self, _data: TupleData=None) -> None:
        """ Добавление виджетов на форму """
        label_id = QLabel(f"ID #{_data[0]}" if _data else "ID")
        label_id.setMinimumSize(QSize(0, HEIGHT_WIDGETS))
        self.gridlayout.addWidget(label_id, 0, 0, 1, 2)

        le = QLineEdit()
        if _data: le.setText(_data[1])
        le.setPlaceholderText(list(head_films.keys())[1])
        le.setMinimumSize(QSize(0, HEIGHT_WIDGETS))
        self.gridlayout.addWidget(le, 1, 0, 1, 2)

        for index, item in enumerate(head_films.keys()):
            if head_films[item] is None: continue
            combobox = QComboBox()
            combobox.addItems(head_films[item])
            combobox.setCurrentIndex(head_films[item].index(_data[index]) if _data else 0)
            combobox.setMinimumSize(QSize(0, HEIGHT_WIDGETS))
            self.gridlayout.addWidget(combobox, index, 0, 1, 2)
        self.gridlayout.addWidget(self.pbOk, index+1, 0, alignment=Qt.AlignLeft | Qt.AlignBottom)
        self.gridlayout.addWidget(self.pbCancel, index+1, 1, alignment=Qt.AlignRight | Qt.AlignBottom)

    # def getDataFromWidgets(self) -> None:
    #     pass


class Ui_FormAdd(Ui_PopupForm):
    """ Форма для добавления данных """
    def __init__(self):
        super().__init__()
        # Название окна
        self.setWindowTitle(WN.FORM_ADD.value)
        # Размер окна
        self.setMinimumSize(QSize(int(WIDTH/2), (HEIGHT_WIDGETS+self.margin)*self.count_widgets))
        self.setMaximumSize(QSize(int(WIDTH/2), (HEIGHT_WIDGETS+self.margin)*self.count_widgets))
        self.addWidgetsForForm()


class Ui_FormEdit(Ui_PopupForm):
    """ Форма для редактирования данных """
    def __init__(self):
        super().__init__()
        # Название окна
        self.setWindowTitle(WN.FORM_EDIT.value)
        # Размер окна
        self.setMinimumSize(QSize(int(WIDTH/2), (HEIGHT_WIDGETS+self.margin)*self.count_widgets))
        self.setMaximumSize(QSize(int(WIDTH/2), (HEIGHT_WIDGETS+self.margin)*self.count_widgets))
