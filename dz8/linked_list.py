import os
from pathlib import  Path

try:
    from format import Format
    from node import Node
except ImportError:
    from .format import Format
    from .node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def build_by_dir(self,path_i: Path):
        for p, d, f in os.walk(path_i):
            for dir_ in d:
                self.append(Node(Path(p, dir_)))
            for file in f:
                self.append(Node(Path(p, file)))

    def append(self, node: Node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def __len__(self):
        out = 0
        node: Node = self.head
        while node:
            node = node.next
            out += 1
        return out

    def __iter__(self):
        self.walk_node: Node = self.head
        return self

    def __next__(self):
        if self.walk_node:
            nxt = self.walk_node
            self.walk_node = self.walk_node.next
            return nxt
        else:
            raise StopIteration

    def __repr__(self):
        return f"""Linked list({len(self)})"""

