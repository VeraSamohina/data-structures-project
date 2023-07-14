class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if self.head is not None:
            node = Node(data, self.head)
            self.head = node
        elif self.head is None:
            node = Node(data)
            self.head = self.tail = node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if self.head is not None:
            node = Node(data)
            self.tail.next_node = node
            self.tail = node
        elif self.head is None:
            node = Node(data)
            self.tail = self.head = node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self) -> list:
        """
        Возвращает список с данными, содержащимися в `LinkedList`
        """
        lst = []
        self.current = self.head
        while self.current is not None:
            lst.append(self.current.data)
            self.current = self.current.next_node
        return lst

    def get_data_by_id(self, id) -> dict:
        """
        Возвращает первый найденный в `LinkedList` словарь с ключом 'id'
        return: словарь из 'LinkedList' по ключу id
        """
        for dct in self.to_list():
            try:
                id_in_dct = dct['id']
                if id == id_in_dct:
                    return dct
            except TypeError:
                print('Данные не являются словарем или в словаре нет id')
