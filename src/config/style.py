from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class FontStyle:
    """ Список шрифтов и их размеров """
    CORBEL = "Corbel"
    SIZE_1 = 1
    SIZE_5 = 5
    SIZE_20 = 25


@dataclass(slots=True, frozen=True)
class Pallete:
    """ Цветовая палитра """
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    DARK_RED = "#D72323"
    ORANGE = "#FF9C00"
    LIGHT_GREY = "#CED6E0"
    DARK_BLUE = "#283149"
    LIGHT_BLUE = "#FFFFFF"  # "#4C5C8A"
