from typing import Any, Optional


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data),


class LinkedList:
    size_counter = 0

    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def append(self, elem: Node):
        new_node = Node(elem)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            self.tail = new_node

        else:
            self.head = new_node
            self.tail = new_node
        self.size_counter += 1

    def pop(self):
        if self.tail:
            if self.head == self.tail:
                popped_elem = self.tail
                self.tail, self.head = None, None
                return popped_elem
            else:
                popped_elem = self.tail
                while current.next.next:
                    current = current.next
                self.tail = current
                self.size_counter -= 1
                return popped_elem
        raise IndexError(f'list is empty')

    def print_list(self):
        if self.head:
            current = self.head
            print(current)
            while current.next:
                print(current.data)
                current = current.next
        else:
            print('list is empty')

    def insert(self, index: int, data: Node):
        if index < 0:
            raise ValueError('index can not be negative')

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        position = 0

        while current and position < index - 1:
            current = current.next
            position += 1

        if not current:
            raise IndexError('Index out of range')

        new_node.next = current.next
        current.next = new_node

    def slice(self, start: int, stop: int):
        if self.head:
            current = self.head
            index = 0
            temp_lst = []
            lst = []
            while current.next:
                temp_lst.append(current.data)
                current = current.next
            for i in range(start - 1, stop - 1):
                lst.append(temp_lst[i])
            return lst

        return f'index out of range'


if __name__ == '__main__':
    linked_lst = LinkedList()
    e1 = Node(1)
    e2 = Node(2)
    e3 = Node(3)
    e4 = Node(4)
    e5 = Node(5)
    e6 = Node(6)
    linked_lst.append(e1)
    linked_lst.append(e2)
    linked_lst.append(e3)
    linked_lst.append(e4)
    linked_lst.append(e5)
    linked_lst.append(e6)
    # linked_lst.print_list()

    print(linked_lst.slice(1, 5))
