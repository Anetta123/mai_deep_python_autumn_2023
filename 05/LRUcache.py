"""Этот модуль реализует LRU-cache"""
from DoubleLinkedList import Node, DoubleLinkedList
from HashMap import HashMap


# Если при добавлении, места еще есть в dll,
# то просто добавляем в голову (добавляем запись в хэш-таблицу),

# если мест нет, то удаляем элемент из хвоста
# (и из хэш-таблицы тоже не забываем) и все равно добавляем в голову

# Когда смотрим элемент, то его нужно удалить из текущего положения в dll: с
# мотрим по хэш таблице ссылку на него --> делаем удаление,
# а затем добавляем в голову (обновляя положение)


class LRUCache:
    def __init__(self, capacity=42):
        self.capacity = capacity
        self.ddl = DoubleLinkedList(capacity)
        self.hm = HashMap(capacity)

    def get(self, key: str):
        x = self.hm.get_val(key)
        if x is not None:
            self.ddl.delete(x)
            self.ddl.insert(x)
            return x.value
        return None

    def set(self, key: str, value: str):
        if self.ddl.current_size == self.ddl.capacity:
            deleted = self.ddl.pop()
            self.hm.delete_val(deleted.key)
        add = Node(key, value)
        self.ddl.insert(add)
        self.hm.set_val(key, add)


cache = LRUCache(2)

cache.set("k1", "val1")
cache.set("k2", "val2")

assert cache.get("k3") is None
assert cache.get("k2") == "val2"
assert cache.get("k1") == "val1"

cache.set("k3", "val3")

assert cache.get("k3") == "val3"
assert cache.get("k2") is None
assert cache.get("k1") == "val1"
