# QUEUE

from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data}'


class Queue:
    size_counter = 0

    def __init__(self):
        self.head = None

    def append(self, val: Node):
        new_node = Node(val)
        if self.head is not None:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
        self.size_counter += 1

    def pop(self) -> Any:
        if self.head is None:
            raise IndexError('queue is empty')
        popped_elem = self.head.data
        self.head = self.head.next
        self.size_counter -= 1
        return popped_elem

    def get_size(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def __len__(self):
        return self.get_size()

    def __str__(self):
        if self.head is None:
            return f'Queue is empty'
        result = "["
        node = self.head
        while node:
            result += str(node.data) + ', '
            node = node.next
        result += "]"

        return result


def handle_queue(queue: Queue):
    while queue.get_size() > 0:
        queue.pop()
        print(f"q: {queue}")


elem1 = Node(1)
elem2 = Node(2)
elem3 = Node(3)
elem4 = Node(4)
elem5 = Node(5)

if __name__ == '__main__':
    values = [elem1, elem2, elem3, elem4, elem5]
    q = Queue()
    for val in values:
        q.append(val)
    print(f"q: {q}")

    handle_queue(q)
