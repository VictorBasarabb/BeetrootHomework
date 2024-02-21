from typing import Any


class NotFoundError(Exception):
    pass


class ElementNotFoundError(NotFoundError):
    pass


class Queue:
    def __init__(self):
        self._storage = []

    def pop(self, ) -> Any:
        self._storage.pop(0)

    def append(self, val: Any) -> None:
        self._storage.append(val)

    def get_size(self):
        return len(self._storage)

    def get_from_queue(self, e: Any) -> Any:
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


def handle_queue(queue: Queue):
    while queue.get_size() > 0:
        queue.pop()
        print(f"q: {queue}")


if __name__ == "__main__":

    num_of_elements = int(input('Enter amount of elements in queue: '))
    q = Queue()
    for i in range(num_of_elements):
        element = input(f'Enter element № {i + 1}: ')
        q.append(element)

    print(f"queue: {q}")

    q.get_from_queue('2')

    handle_queue(q)
    print(f"queue: {q}")

