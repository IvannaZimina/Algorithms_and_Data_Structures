# Add a relevant code to Tree class in order to proper work of method degree(self, node_id: int) -> int
# Don't change the code after if __name__ == "__main__": for tests to able to processed properly

from typing import Any, Type

# Stack - Last in, first out (LIFO)
# Placed on top: [A]
# Put another one: [A, B]
# Put another one: [A, B, C]

# Can ONLY be removed from the top → C

class Stack:
    def __init__(self):
        self.stack = [] # list to hold stack items

    def push(self, item):
        self.stack.append(item) # always add item to the end of the list

    def pop(self):
        if not self.is_empty():
            # delete the last item and return it
            # ['A', 'B', 'C'].pop() -> 'C' and stack becomes ['A', 'B']
            # why without index? - pop() == pop(len(list)-1) default behavior

            # s.stack = ['A', 'B', 'C']
            # x = s.pop()

            # x = 'C'
            # stack = ['A', 'B']

            return self.stack.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            # ['A', 'B', 'C'][-1] → 'C' - look at the last item without removing it
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

# save the structure of the tree in the form of adjacency list
class Node:
    def __init__(self, node_id: int, data: Any, parent: Type['Node'] = None) -> None:
        self.id = node_id
        self.data = data
        self.parent = parent
        self.child = []

    def __repr__(self) -> str:
        return f"N{self.id}({self.data})"

# manage the tree structure and provide methods to manipulate it
# LIFO → stack → DFS
class Tree:
    def __init__(self, root_data: Any) -> None:
        self.root = Node(0, root_data)  # tree = Tree('A'), root = A (id=0)
        self.map = {0: self.root}       # dictionary id → Node, {  0: Node(A) }

    # child_data → node value (e.g. 'B')
    # to_node_id → parent to add to
    def add_child(self, child_data: Any, to_node_id: int = 0) -> Node:
        # map[key] → value, map[0] → root node
        # self.map = {  0: A,  1: B }, to_node_id = 1, parent = B
        parent = self.map[to_node_id]

        # we get the number of nodes in the tree, and use it as the id for the new node
        # map = {0: A, 1: B}, len = 2 - the way to generate new id for the new node
        last_id = len(self.map)

        # create a new node with the generated id, the provided data, and the parent node: Node(2, 'C', parent=B)
        new_node = Node(last_id, child_data, parent)

        # was: B.child = [], after appending:B.child.append(C) → B.child = [C]
        parent.child.append(new_node)

        # save to the dictionary the new node with its id as the key: map[2] = C
        # was: {0: A, 1: B}, after adding new node: {0: A, 1: B, 2: C}
        self.map[last_id] = new_node

        return new_node

        # ======== How it works: = ========

        # tree = Tree('A')
        # map = {0: A}
        # B = tree.add_child('B')

        # parent = A
        # last_id = 1
        # создаём B(1)
        # A.child = [B]
        # map = {0: A, 1: B}

        # C = tree.add_child('C')

        # parent = A
        # last_id = 2
        # A.child = [B, C]
        # map = {0: A, 1: B, 2: C}

        #     A
        #    / \
        #   B   C

    def __iter__(self):
        # helps to get around the tree structure and visit each node in the tree
        stack = Stack()
        stack.push(self.root) # [A]

        while not stack.is_empty():
            # take the TOP element from the stack and remove it
            # stack = [A, B, C], pop() → current = C, stack = [A, B]
            current: Node = stack.pop() # almost always it is a DFS, but it can be BFS if we add children in reverse order

            # take the list of children of the current node
            # current = A, A.child = [B, C]
            for child in current.child:
                stack.push(child)

            # does not terminate the function,
            # remembers the state,
            # returns the next element on each iteration

            # Example:
            # for node in tree:
            #     print(node)
            # each time yield gives the next node

            yield current

    # How iteration works:
    # There is a tree:
    #     A
    #    / \
    #   B   C
    # When we start iterating over the tree, the stack is initialized with the root node A: stack = [A].
    # pop → A is removed from the stack and becomes the current node: current = A, stack = [].
    # The children of A (B and C) are added to the stack: stack = [B, C].
    # yield A → the first node A is returned to the caller.

    # Next iteration:
    # pop → C is removed from the stack and becomes the current node: current = C, stack = [B].
    # C has no children, so nothing is added to the stack.
    # yield C → the second node C is returned to the caller.


    # number of children of a node
    # example:
    # A.child = [B, C] → degree = 2
    # B.child = [D, E] → degree = 2
    # C.child = [] → degree = 0
    def degree(self, node_id: int) -> int:
        return len(self.map[node_id].child)

if __name__ == "__main__":
    tree = Tree('A')
    B = tree.add_child('B')  
    C = tree.add_child('C')

    tree.add_child('D', B.id)
    tree.add_child('E', B.id)
    tree.add_child('F', B.id)

    G = tree.add_child('G', C.id)
    H = tree.add_child('H', G.id)
    
    #           A(0)
    #          /   \
    #      B(1)     C(2)
    #   /   |   \     \
    # D(3) E(4) F(5)   G(6)
    #                   \
    #                   H(7)

    node_id = int(input())
    print(tree.degree(node_id))
    
    tree = Tree('Apple')     # A
    banana = tree.add_child('Banana')      # B
    cherry = tree.add_child('Cherry')      # C

    tree.add_child('Date', banana.id)      # D
    tree.add_child('Elderberry', banana.id) # E
    tree.add_child('Fig', cherry.id)        # F
    tree.add_child('Grape', cherry.id)      # G

    #          Apple
    #        /       \
    #   Banana        Cherry
    #    /   \         /   \
    # Date Elderberry Fig Grape

    # what stores in the Node:
    # Apple.child = [Banana, Cherry]
    # Banana.child = [Date, Elderberry]
    # Cherry.child = [Fig, Grape]

    # stack = [Apple]
    # pop → Apple, stack = []
    # push Banana, Cherry → stack = [Banana, Cherry]
    # pop → Cherry, stack = [Banana]
    # push Fig, Grape → stack = [Banana, Fig, Grape]
    # pop → Grape, stack = [Banana, Fig]
    # pop → Fig, stack = [Banana]
    # pop → Banana, stack = []
    # iteration ends