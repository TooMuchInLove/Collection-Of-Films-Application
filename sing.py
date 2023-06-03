# -*- coding: utf-8 -*-


class Singleton:
    """ Класс для определения единственного экземпляра """
    _instance = None
    def __new__(cls, *args, **kwargs):
        """ Реализует вызов экземпляра класса """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
