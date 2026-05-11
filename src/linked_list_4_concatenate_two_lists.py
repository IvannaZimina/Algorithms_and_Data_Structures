from linked_list_1_fruits_example import LinkedList

class ExtendedLinkedList(LinkedList):
    """
    Extended version of LinkedList
    that adds concatenation functionality.
    """

    def concat(self, other):
        """
        Concatenate two linked lists into a NEW linked list.

        self  -> first linked list
        other -> second linked list
        returns -> new LinkedList with combined values
        """

        result = LinkedList()
        # [apple] -> [banana] -> [cherry] -> [mango] -> [orange] -> [pineapple] -> None

        # copy elements from the first list
        current_first = self.head
        while current_first is not None:
            result.insert_at_tail(current_first.value)
            current_first = current_first.next

        # copy elements from the second list
        current_second = other.head
        while current_second is not None:
            result.insert_at_tail(current_second.value)
            current_second = current_second.next

        return result

if __name__ == "__main__":

    # Create two linked lists
    basket1 = ExtendedLinkedList()
    basket2 = LinkedList()

    # Fill the first linked list (basket 1)
    # basket1: apple -> banana -> cherry
    basket1.insert_at_tail("apple")
    basket1.insert_at_tail("banana")
    basket1.insert_at_tail("cherry")

    # Fill the second linked list (basket 2)
    # basket2: mango -> orange -> pineapple
    basket2.insert_at_tail("mango")
    basket2.insert_at_tail("orange")
    basket2.insert_at_tail("pineapple")

    print("Basket 1 (first linked list):")
    basket1.display()

    print("Basket 2 (second linked list):")
    basket2.display()

    print("Concatenated basket (new linked list):")
    combined_basket = basket1.concat(basket2)
    combined_basket.display()

# === Output ===
# Basket 1 (first linked list):
# apple -> banana -> cherry
# Basket 2 (second linked list):
# mango -> orange -> pineapple
# Concatenated basket (new linked list):
# apple -> banana -> cherry -> mango -> orange -> pineapple
