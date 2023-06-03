# -*- coding: utf-8 -*-

# from config import FontFamily as FF
from config import FontStyle as FS
from config import Pallete as PL


# Стиль всплывающей ошибки
S_ERROR = f"""
background: {PL.WHITE.value};\n
color: {PL.DARK_RED.value};\n
border: {FS.SIZE_1.value}px solid {PL.DARK_RED.value};\n
"""

# Стиль всплывающего уведомления
S_NOTIFICATION = f"""
background: {PL.DARK_BLUE.value};\n
color: {PL.WHITE.value};\n
border: {FS.SIZE_1.value}px solid {PL.WHITE.value};\n
"""

# Светлая тема приложения
LIGHT_THEME = f"""
QWidget {{\n
    font-family: {FS.CORBEL.value};\n
    font-size: {FS.SIZE_15.value}px;\n
    background: {PL.WHITE.value};\n
    color: {PL.DARK_BLUE.value};\n
}}\n

QPushButton {{\n
    background: {PL.LIGHT_BLUE.value};\n
    color: {PL.WHITE.value};\n
}}\n

QPushButton:hover {{\n
    background: {PL.LIGHT_GREY.value};\n
}}\n

QLabel, QPushButton, QLineEdit {{\n
    padding: 0 {FS.SIZE_5.value}px;\n
}}\n

QPushButton, QLineEdit, QComboBox, QLabel {{\n
    border-radius: {FS.SIZE_5.value}px;\n
}}\n

QLineEdit, QComboBox {{\n
    border: {FS.SIZE_1.value}px solid {PL.LIGHT_GREY.value};\n
}}\n

QLineEdit:focus, QComboBox:focus {{\n
    border-color: {PL.ORANGE.value};\n
}}\n
"""
# QTableWidget, QTableWidgetItem {{\n
#     background: {PL.DARK_BLUE.value};\n
#     color: {PL.WHITE.value};\n
# }}\n
# """
