from math import floor, log2


class MinHeap:
    def __init__(self):
        self.heap = []

    def size(self):
        """return the number of nodes in the heap"""
        return len(self.heap)

    def is_empty(self):
        """check if the heap is empty"""
        return len(self.heap) == 0

    def __str__(self):
        """string representation of a heap"""
        return str(self.heap)

    def swap(self, i, j):
        """swap the heap elements"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def parent(self, index):
        """calculate the index of a node's parent"""
        return (index - 1) // 2

    def left_child(self, index):
        """calculate the index of a node's left child"""
        return 2 * index + 1

    def right_child(self, index):
        """calculate the index of a node's right child"""
        return 2 * index + 2

    def has_parent(self, index):
        """check if a node at a given index has a parent"""
        return self.parent(index) >= 0

    def has_left_child(self, index):
        """check if a node at a given index has a left child"""
        return self.left_child(index) < len(self.heap)

    def has_right_child(self, index):
        """check if a node at a given index has a right child"""
        return self.right_child(index) < len(self.heap)

    def _level(self, index) -> int:
        """Returns level on which node places"""
        return floor(log2(index + 1))

    def display(self) -> None:
        """Displays heap as a tree in console"""
        levels = self._level(self.size() - 1) + 1
        symbols = max(len(str(x)) for x in self.heap)
        row = ""

        for i, elem in enumerate(self.heap):
            current_level = self._level(i)
            distance = 2 ** (levels - current_level) * symbols

            # Printing Node
            elem_str = f"{elem if elem else '' : ^{symbols}}"
            print(f"{elem_str : ^{distance}}", end="", sep="")

            # Adding Edges for existing childs
            lines = "/" if self.has_left_child(i) else " "
            lines += " " * symbols
            lines += "\\" if self.has_right_child(i) else " "
            row += f"{lines:^{distance}}"

            # At the end of level add Edges row
            if i + 1 == (2 ** (current_level + 1) - 1):
                print()
                lines = '/ \\'
                print(row, sep="")
                row = ""

        print()


if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.heap = [12, 15, 25, 16]
    min_heap.display()
