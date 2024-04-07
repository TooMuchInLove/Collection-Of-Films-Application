from dataclasses import dataclass


@dataclass(slots=True)
class ContainerWidget:
    """ Хранилище для объекта (виджет) и его идентификатора (тэг) """
    obj: object
    tag: str
