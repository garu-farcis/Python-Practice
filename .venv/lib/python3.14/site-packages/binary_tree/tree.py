from binary_tree.node import *


class tree:
    def search(self, n):
        return self.root.search(n)

    def addNode(self, n):
        if self.root:
            self.root.addValue(n)

    def traverse(self):
        return self.root.visit()

    def __str__(self):
        s = ''
        for n in self.traverse():
            s += f'{str(n)}, '
        return s

    def __repr__(self):
        self.traverse()

    def __init__(self, list):
        self.root = node(list[0])

        for n in list[1:]:
            self.addNode(n)
