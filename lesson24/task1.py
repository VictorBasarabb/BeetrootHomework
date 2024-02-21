import time
from typing import Any


class Stack:
    last_item = None

    def __init__(self):
        self._storage = []

    def pop(self, ) -> Any:
        self.last_item = self._storage.pop()
        return self.last_item

    def append(self, val: Any):
        self._storage.append(val)

    def get_size(self):
        return len(self._storage)

    def __len__(self):
        return self.get_size()

    def __str__(self):
        return f"{self._storage}"

    def __bool__(self):
        return bool(self.get_size())

    def __reversed__(self):
        return self._storage[::1]


def process(lst):
    time.sleep(0.5)
    print(f"process: {lst} ")


def handle_stack(stack: Stack):
    reversed_vals = []
    while len(stack) > 0:
        reversed_vals.append(stack.pop())
        process(reversed_vals)
    print(f'reversed: {reversed_vals}')


if __name__ == "__main__":

    values = input(f"Users: ")
    s = Stack()
    for value in values:
        s.append(value)
    print(f"default: {s}")

    handle_stack(s)
