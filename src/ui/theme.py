from src.config import FontStyle as FS, Pallete as PL

# Стиль всплывающей ошибки
S_ERROR = f"""
background: {PL.WHITE};\n
color: {PL.DARK_RED};\n
border: {FS.SIZE_1}px solid {PL.DARK_RED};\n
"""

# Стиль всплывающего уведомления
S_NOTIFICATION = f"""
background: {PL.DARK_BLUE};\n
color: {PL.WHITE};\n
border: {FS.SIZE_1}px solid {PL.WHITE};\n
"""

# Светлая тема приложения
LIGHT_THEME = f"""
QWidget {{\n
    font-family: {FS.CORBEL};\n
    font-size: {FS.SIZE_20}px;\n
    background: {PL.WHITE};\n
    color: {PL.DARK_BLUE};\n
}}\n

QPushButton {{\n
    background: {PL.LIGHT_BLUE};\n
    color: {PL.WHITE};\n
}}\n

QPushButton:hover {{\n
    background: {PL.LIGHT_GREY};\n
}}\n

QLabel, QPushButton, QLineEdit {{\n
    padding: 0 {FS.SIZE_5}px;\n
}}\n

QPushButton, QLineEdit, QComboBox, QLabel {{\n
    border-radius: {FS.SIZE_5}px;\n
}}\n

QLineEdit, QComboBox {{\n
    border: {FS.SIZE_1}px solid {PL.LIGHT_GREY};\n
}}\n

QLineEdit:focus, QComboBox:focus {{\n
    border-color: {PL.ORANGE};\n
}}\n
"""
