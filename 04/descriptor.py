"""Descriptor module"""


class Integer:
    """Integer Descriptor"""

    def __init__(self, min_value: int, max_value: int):
        """Initializator"""
        self.min = min_value
        self.max = max_value

    def __set_name__(self, owner, name):
        """The name setter"""
        self.name = name

    def __get__(self, instance, owner):
        """Getter"""
        if self.name in instance.__dict__:
            return instance.__dict__[self.name]
        raise ValueError("There is no value here")

    def __set__(self, instance, value):
        """Setter"""
        if isinstance(value, int) and self.min <= value <= self.max:
            instance.__dict__[self.name] = value
        else:
            raise ValueError("Check your data!")


class String:
    def __init__(self, min_length: int, max_length: int):
        """String Descriptor"""
        self.min = min_length
        self.max = max_length

    def __set_name__(self, owner, name):
        """The name setter"""
        self.name = name

    def __get__(self, instance, owner):
        """Getter"""
        if self.name in instance.__dict__:
            return instance.__dict__[self.name]
        else:
            raise ValueError("There is no value here")

    def __set__(self, instance, value: str):
        """Setter"""
        if isinstance(value, str) and (self.min <= len(value) <= self.max):
            instance.__dict__[self.name] = value
        else:
            raise ValueError("Check your data!")


class PositiveInteger:
    """Positive Integer Descriptor"""

    def __init__(self, min_: int, max_: int):
        self.min_ = min_
        self.max_ = max_

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if self.name in instance.__dict__:
            return instance.__dict__[self.name]
        else:
            raise ValueError("There is no value here")

    def __set__(self, instance, value: str):
        if isinstance(value, int) and value > 0 and self.min_ <= value <= self.max_:
            instance.__dict__[self.name] = value
        else:
            raise ValueError("Check your data!")


class Data:
    age = Integer(18, 40)
    name = String(5, 10)
    price = PositiveInteger(2000, 5000)

    def __init__(self, age, name, price):
        self.age = age
        self.name = name
        self.price = price

    def __str__(self):
        return f"Obj with age: {self.age}, name: {self.name}, price: {self.price}"
