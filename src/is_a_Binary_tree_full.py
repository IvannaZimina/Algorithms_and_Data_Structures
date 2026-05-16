# Add a relevant code to Tree class in order to proper work of method is_full(self) -> bool
# Don't change the code after if __name__ == "__main__": for tests to able to processed properly

from re import match
from typing import Any, Type


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def display(self, message: str = None):
        print(
            (f"{message}: " if message else "") +
            f"{self.stack}"
        )


class BinaryNode:
    def __init__(self, BinaryNode_id: int, data: Any, parent: Type['BinaryNode'] = None) -> None:
        self.id = BinaryNode_id
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"bN{self.id}({self.data})"


class BinaryTree:
    def __init__(self, root_data: Any) -> None:
        self.root = BinaryNode(0, root_data)
        self.map = {0: self.root}

    def add_child(self, child_data: Any, to_node_id: int = 0) -> BinaryNode:
        parent = self.map[to_node_id]
        last_id = len(self.map)
        new_node = BinaryNode(last_id, child_data, parent)
        if not parent.left:
            parent.left = new_node
        elif not parent.right:
            parent.right = new_node
        else:
            raise Exception(
                "In BinaryTree one can't be added more than 2 Nodes to parent")
        self.map[last_id] = new_node

    def __iter__(self):
        stack = Stack()
        stack.push(self.root)

        while not stack.is_empty():
            # take the TOP element from the stack, it becomes the current node and remove it from the stack
            current: BinaryNode = stack.pop()

            # first fill the left child
            if current.left:
                stack.push(current.left)

            # then fill the right child
            if current.right:
                stack.push(current.right)

            yield current # makes the class iterable

    # each node has either 0 or 2 children
    def is_full(self) -> bool:
        for node in self:
            # first case: both children are present — ok
            if node.left and node.right:
                continue

            # second case: both children are absent — ok
            if not node.left and not node.right:
                continue

            # third case: only one child is present — not full
            return False

        return True


if __name__ == "__main__":
    tree = BinaryTree(1)
    line_num = int(input())

    for _ in range(line_num):
        line = input()

        # (?P<parent_id>\d+) - number → parent_id
        # (?P<left>\d+)? - left child (may be absent)
        # (?P<right>\d+)? - right child (may be absent)
        res = match(r'(?P<parent_id>\d+): (?P<left>\d+)? ?(?P<right>\d+)?\s*', line)

        # If there is a left child, add it to parent
        if res['left']:
            tree.add_child(int(res['left']), int(res['parent_id']))

        # If there is a right child, add it to parent
        if res['right']:
            tree.add_child(int(res['right']), int(res['parent_id']))

    print(tree.is_full())

    #     A
    #    / \
    #   B   C
    #  / \ / \
    # D  E F  G

# === Input ===
# 3
# 0: 2 3
# 1: 4 5
# 2: 6 7

# === Output ===
# True
