#   STACK
from typing import Any


class NotFoundError(Exception):
    pass


class ElementNotFoundError(NotFoundError):
    pass


class Stack:
    def __init__(self):
        self._storage = []

    def pop(self, ) -> Any:
        self._storage.pop()

    def append(self, val: Any):
        self._storage.append(val)

    def get_size(self):
        return len(self._storage)

    def get_from_stack(self, e: Any) -> Any:
        searched_element = None
        for index, elem in enumerate(self._storage):
            if elem == e:
                searched_element = e
                self._storage[index] = None
                return searched_element

        if searched_element is None:
            raise ElementNotFoundError(f'there is no such element in stack: <{e}>')

    def __len__(self):
        return self.get_size()

    def __str__(self):
        return f"{self._storage}"

    def __bool__(self):
        return bool(self.get_size())


def handle_stack(stack: Stack):
    while stack.get_size() > 0:
        stack.pop()
        print(f"q: {stack}")


if __name__ == "__main__":

    num_of_elements = int(input('Enter amount of elements in stack: '))
    s = Stack()
    for i in range(num_of_elements):
        element = input(f'Enter element № {i + 1}: ')
        s.append(element)

    print(f"stack: {s}")

    s.get_from_stack('3')

    handle_stack(s)
    print(f"stack: {s}")

