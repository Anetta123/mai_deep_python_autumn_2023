"""Meta Class implementation"""


class CustomMeta(type):
    """Meta Class"""

    def __new__(mcs, name: str, bases: tuple, attrs: dict):
        # Так как есть доступ к атрибутам класса,
        # то можно переопределить __setattr__ следующей функцией
        def custom_setattr(self, _name, _value):
            self.__dict__["custom_" + _name] = _value

        # Опять же, в связи с тем, что есть связь с атрибутами,
        # то можем пройтись по ним всем и дописать к ним "custom_"
        new_attrs = {}
        for attr, value in attrs.items():
            if not (attr.startswith("__") and attr.endswith("__")):
                new_attrs["custom_" + attr] = value
            else:
                new_attrs[attr] = value

        # Подменяем атрибут
        new_attrs["__setattr__"] = custom_setattr

        # Вызываем конструктор с новым словарем атрибутов
        obj = super().__new__(mcs, name, bases, new_attrs)

        return obj


class CustomClass(metaclass=CustomMeta):
    x = 50
    y = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"
