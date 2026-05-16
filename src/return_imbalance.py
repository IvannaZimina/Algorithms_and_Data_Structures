# Add a relevant code to Tree class in order to proper work of method root_imbalance(self) -> str
# Method above returns 'Balanced' if root is balanced, or type of imbalance otherwise (i.e. 'LL')
# Don't change the code after if __name__ == "__main__": for tests to able to processed properly

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
        # True - if there any child exists, False - if there is no children
        return not (self.left or self.right)

    @property
    def height(self) -> int:
        # leaf - height = 0, otherwise node with children = max(height of children) + 1
        if self.is_leaf():
            return 0

        # use recursion to calculate height of children
        # height of left and right child, if they exist, otherwise 0
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0

        # height calculated from bottom to top, because height of current node depends on height of children
        # === example 1 ===
        #     A
        #    /
        #   B
        #  /
        # C

        # C (no children) → height = 0
        # B (one child with height 0) → height = max(0, 0) + 1 = 1
        # A (one child with height 1) → height = max(1, 0) + 1 = 2

        # === example 2 ===
        #     A
        #    / \
        #   B   C
        #  /
        # D

        # D (no children) → height = 0
        # B (one child with height 0) → height = max(0, 0) + 1 = 1
        # C (no children) → height = 0
        # A (two children with heights 1 and 0) → height = max(1, 0) + 1 = 2


        # height of current node = max(height of left, right child) + 1
        # Because height = longest way down
        return max(left_height, right_height) + 1
    
    # example:
    #     A
    #    /
    #   B
    #  /
    # C

    # C → 0
    # B → 1
    # A → 2

    def __repr__(self) -> str:
        return f"avlN{self.id}({self.data},h={self.height})"

    # |bf| = absolute value: |2| = 2, |-2| = 2
    # if |bf| ≤ 1 → balanced
    # if |bf| ≥ 2 → unbalanced
    def bf(self) -> int:
        # with the property height we can calculate balance factor of the node
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        return left_height - right_height


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
        
    def root_imbalance(self) -> str:
        # bf = height(left) − height(right).
        root_bf = self.root.bf()

        # Balanced if the balance factor is -1, 0, or 1.
        if -1 <= root_bf <= 1:
            return "Balanced"

        # If bf > 1, then the left subtree is too high - this is a left-side imbalance.
        if root_bf > 1:
            # If the left child is "leaned" to the left (bf ≥ 0), it is LL.
            # If the left child is "leaned" to the right (bf < 0), it is LR.
            left_bf = self.root.left.bf() if self.root.left else 0
            return "LL" if left_bf >= 0 else "LR"

        right_bf = self.root.right.bf() if self.root.right else 0
        return "RR" if right_bf <= 0 else "RL"

        # bf ∈ {..., -3, -2, -1, 0, 1, 2, 3, ...}
        # BUT
        # for AVL tree should be bf ∈ {-1, 0, 1}
        # if bf = 2 or -2 → is indicated that tree unbalanced

if __name__ == "__main__":
    from re import match

    tree = AVLTree(1)
    line_num = int(input())

    for _ in range(line_num):
        line = input()

        # (?P<parent_id>\d+) - number → parent_id
        # (?P<left>\d+)? - left child (may be absent)
        # (?P<right>\d+)? - right child (may be absent)
        res = match(
            r'(?P<parent_id>\d+): (?P<left>\d+)? ?(?P<right>\d+)?\s*', line)

        if res['left']:
            tree.add_child(int(res['left']), int(res['parent_id']))
        if res['right']:
            tree.add_child(int(res['right']), int(res['parent_id']))

    print(tree.root_imbalance())

# === input ===
# 3
# 0: 2 3
# 1: 4 5
# 2: 6

# === output ===
# Balanced