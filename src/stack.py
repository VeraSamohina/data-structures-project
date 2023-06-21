class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        :param next_node: узел, созданный до текущего. Когда создается первый экземпляр класса, то равен None
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.stack = []
        # Указатель вершины стека. Для пустого стека - None
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        self.data = data
        node = Node(data)
        self.stack.append(self.data)
       # После добавления элемента в стек, меняем указатель вершины стека и предыдущего узла
        node.next_node = self.top
        self.top = node


    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        pass
