from typing import (
    Optional,
    Any,
)


class Category:
    def __init__(self, name: str, parent: Optional["Category"] = None):
        self.name = name
        self._children = []
        self._parent = parent
        if self.parent is not None:
            self._parent._children.append(self)

    def __str__(self):
        return self.name

    @property
    def parent(self):
        return self._parent

    @property
    def children(self):
        return self._children

    def insert(self, tree: "Category"):
        tree._parent = self
        self._children.append(tree)

    def remove_tree(self, tree: "Category"):
        if tree in self._children:
            self._children.remove(tree)
            tree._parent = None
        else:
            raise ValueError("Tree not found")


def print_tree(category: Category, ident: int = 0):
    print('--' * ident, category)
    for child in category.children:
        # print(f"  {child}")
        print_tree(child, ident + 1)


# def find(category: Category, name: str) -> Optional[Category]:
#     print(f"... {category}")
#     if category.name == name:
#         return category
#
#     for child in category.children:
#         value = find(child, name)
#         if value is not None:
#             return value
#
#     return None


if __name__ == '__main__':
    strings = Category("strings", parent=None)
    beats = Category("beats", parent=None)
    guitars = Category("guitars", parent=strings)
    violins = Category("violins", parent=strings)
    drums = Category("drums", parent=beats)
    acoustics = Category("acoustics", parent=guitars)
    electrics = Category("electrics", parent=guitars)
    alt = Category("alt", parent=violins)
    fenders = Category("fenders", parent=electrics)
    gibsons = Category("gibsons", parent=electrics)
    beats = Category("beats", parent=strings)

    print_tree(strings, 1)
    strings.remove_subtree(guitars)
    print("===")
    print_tree(strings, 1)
    strings.insert(guitars)
    print("===")
    print_tree(strings, 1)



    # print("===")
    # cat = find(strings, "123456")
    # print(cat)
