from dataclasses import dataclass
from .base import IMAGES_PATH


@dataclass(slots=True, frozen=True)
class SettingsApplication:
    """ Настройки окна приложения """
    title: str = "Collection of films"  # название окна приложения
    width: int = 1050  # ширина окна приложения
    height_min: int = 700  # минимальная высота окна приложения
    height_max: int = 1000  # максимальная высота окна приложения
    height_widgets: int = 50  # высота компонентов в приложении
    margin: int = 30  # внутренняя рамка для окна приложения
    max_len_field: int = 100  # максимальная длина строки в поле


@dataclass(slots=True, frozen=True)
class ImagesApplication:
    """ Различные лого и иконки для приложения и виджетов """
    icon_save = f"{IMAGES_PATH}/save.png"
    icon_add = f"{IMAGES_PATH}/add.png"
    icon_view = f"{IMAGES_PATH}/view.png"
    icon_delete = f"{IMAGES_PATH}/delete.png"
    icon_close = f"{IMAGES_PATH}/close.png"


@dataclass(slots=True, frozen=True)
class WidgetName:
    """ Список названий виджетов приложения (и главные окна) """
    TITLE = "Collection of films"
    FORM_ADD = "Добавить запись"
    FORM_EDIT = "Редактировать запись"
    FORM_DEL = "Удалить выбранные данные?"
    FORM_VIEW = "Просмотр данных"


settings_app = SettingsApplication()

images_app = ImagesApplication()
