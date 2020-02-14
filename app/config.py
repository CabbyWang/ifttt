# coding:utf-8

from importlib import import_module


class Sington:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance
        return super().__new__(cls, *args, **kwargs)


class Config(Sington):

    def __init__(self):
        self._config = {}

    def from_object(self, obj):
        obj = import_module(obj)
        for key in dir(obj):
            if key.isupper():
                self._config[key] = getattr(obj, key)

    def __getitem__(self, key):
        return self._config.get(key)

    def __setitem__(self, key, value):
        self._config[key] = value
