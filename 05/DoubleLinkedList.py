# Двусвязный список нужен, чтобы сделать упорядоченность по времени использования,
# так как мы имеем укзазатели на голову и хвост листа


class Node(object):
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"Node<{self.key}, {self.value}>"


class DoubleLinkedList(object):
    """Класс двусвязного списка"""

    def __init__(self, capacity: int):
        """Инициализируем объект двусвязного списка хвостовым, головным элементом и количеством элементов"""
        self.tail = None
        self.head = None
        self.current_size = 0
        self.capacity = capacity

    def insert(self, obj: Node):
        """ "Это добавление работает в голову двусвязного списка"""
        code = 0
        if self.current_size == 0:
            self.tail = obj
            self.head = obj
            self.current_size = 1
        elif self.current_size < self.capacity:
            self.head.next = obj
            obj.prev = self.head
            self.head = obj
            self.current_size = self.current_size + 1
        else:
            code = 1
        return code

    def pop(self):
        """Это будет удаление из хвоста --> не требуется ссылка, удаление будет и так константным"""
        if self.current_size == 1:
            tmp = self.tail
            self.head = None
            self.tail = None
            self.current_size = self.current_size - 1
        elif self.current_size > 1:
            tmp = self.tail
            tmp.next.prev = None
            self.tail = tmp.next
            self.current_size = self.current_size - 1
        else:
            return None
        return tmp

    def delete(self, obj: Node):
        code = 0
        if self.current_size == 1 and (self.tail == obj or self.head == obj):
            self.current_size = 0
            self.tail = None
            self.head = None
        elif self.current_size > 1:
            if obj == self.tail:
                tmp = self.tail
                tmp.next.prev = None
                self.tail = tmp.next
            elif obj == self.head:
                tmp = self.head
                tmp.prev.next = None
                self.head = tmp.prev
            else:
                obj.prev.next = obj.next
                obj.next.prev = obj.prev
            self.current_size = self.current_size - 1
        else:
            code = 1
        return code