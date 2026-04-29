from typing import Any, Type, Union


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


class AVLNode:
    def __init__(self, AVLNode_id: int, data: Any, parent: Type['AVLNode'] = None) -> None:
        self.id = AVLNode_id
        self.data = data
        self.parent = parent
        self.left: Type['AVLNode'] = None
        self.right: Type['AVLNode'] = None

        # Calc level
        if parent:
            self.level = parent.level + 1
        else:
            self.level = 0

        # self.level = parent + 1 if parent else 0

    def is_leaf(self) -> bool:
        return not (self.left or self.right)

    @property
    def height(self) -> int:
        if self.is_leaf():
            return 0

        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0

        return max(left_height, right_height) + 1

    def __repr__(self) -> str:
        return f"avlN{self.id}({self.data},h={self.height})"


class AVLTree:
    def __init__(self, root_data: Any) -> None:
        self.root = AVLNode(0, root_data)
        self.map = {0: self.root}

    def add_child(self, child_data: Any, to_node: Union[AVLNode, int]) -> AVLNode:
        if isinstance(to_node, AVLNode):
            node_id = to_node.id
        else:
            node_id = to_node

        parent = self.map[node_id]
        last_id = len(self.map)
        new_node = AVLNode(last_id, child_data, parent)
        if not parent.left:
            parent.left = new_node
        elif not parent.right:
            parent.right = new_node
        else:
            raise Exception(
                "In BinaryTree one can't be added more than 2 Nodes to parent")
        self.map[last_id] = new_node
        return new_node

    def __iter__(self):
        stack = Stack()
        stack.push(self.root)

        while not stack.is_empty():
            current: AVLNode = stack.pop()
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)
            yield current

    def display(self) -> None:
        for node in self:
            print("  " * node.level + str(node))
            

if __name__ == "__main__":
    tree = AVLTree('30')
    L = tree.add_child('20', tree.root)
    R = tree.add_child('35', tree.root)
    LL = tree.add_child('10', L)
    LLL = tree.add_child('5', LL)
    LR = tree.add_child('25', L)

    tree.display()