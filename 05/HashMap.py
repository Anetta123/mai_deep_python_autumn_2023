# Хэш-мапа нужна потому что у нас будут по ключу сразу объекты двусвязного списка (ключ + значение),
# чтобы удалять за O(1) из середины двусвязного списка


from DoubleLinkedList import Node


class HashMap(object):
    """Класс, который реализует хэш-таблицу, так как в питоне её нет"""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_table = self.create_buckets(capacity)

    @staticmethod
    def create_buckets(capacity: int):
        """Создаем бакеты"""
        return [[] for _ in range(capacity)]

    def set_val(self, key: str, obj: Node):
        """Устанавливаем значение"""
        hashed_key = hash(key) % self.capacity
        bucket = self.hash_table[hashed_key]

        for index, record in enumerate(bucket):
            key_, obj_ = record
            if key == key_:
                bucket[index] = (key, obj)
                return 1

        bucket.append((key, obj))
        return 0

    def get_val(self, key: str):
        """Получаем значение"""
        hashed_key = hash(key) % self.capacity
        bucket = self.hash_table[hashed_key]

        for index, record in enumerate(bucket):
            key_, obj_ = record
            if key == key_:
                return obj_

        return None

    def delete_val(self, key: str):
        """Удаляем значение"""
        hashed_key = hash(key) % self.capacity
        bucket = self.hash_table[hashed_key]

        for index, record in enumerate(bucket):
            key_, obj_ = record
            if key == key_:
                bucket.pop(index)
                return 1
        return 0
