"""
Step 1
In previous lessons, you learned about some common data structures. In this workshop, you'll implement a linked list.
First, create a class named LinkedList to represent the structure that will hold your list nodes. Add the pass keyword inside the class so that the test can pass.

Step 2
Inside your LinkedList class, replace the pass keyword with an inner class called Node. This will represent individual nodes that store data in the list.

Step 3
Next, remove the pass keyword inside the Node class, then give the Node class an __init__ method with two parameters, self and element.
Inside the method, assign element to self.element. This stores the value passed when creating a node.

Step 4
Still inside the __init__ method, assign None to self.next. This sets the next pointer to None, meaning that the new node does not yet point to any other node in the list.
Later, next can be updated to point to another node to form the chain of a linked list.

Step 5
Inside the LinkedList class, add an __init__ method that sets self.length to 0. This initializes a counter to track how many nodes (elements) are currently in the list.

Step 6
Still in the __init__ method of the LinkedList class, set self.head to None. This acts as a reference to the first node in the list. The list is empty at the moment so, you have to set it to None.

Step 7
Add a method called is_empty that returns self.length == 0.
You'll use this to keep track of how many nodes are in the list. So, with self.length == 0, it returns True, meaning that the list has no nodes.
If self.length is greater than 0, it returns False, meaning that the list has at least one node.

Step 8
Let's test your linked list so far! At the bottom of your code, create an instance of LinkedList called my_list. Then, using the is_empty method you created in the last step, print my_list.is_empty().

Step 9
Now, after the is_empty method, create a method called add inside the LinkedList class. The new method should have two parameters, self and element.
Inside your new method, create a variable named node and assign it a new instance of Node by using self.Node(element). This will create a new node to be added to the linked list.

Step 10
If the list is empty, then the new node becomes the first element (the head). Inside the add method, create an if statement that checks if the list is empty using self.is_empty() and assign node to self.head.

Step 11
If the list is not empty, the method should find the last node and link the new node to its next pointer.
To do this, create an else block after the if block. Inside the else block, create a current_node variable and assign self.head to it.

Step 12
Still inside the else block, create a while loop that checks that current_node.next is not None.
Inside the while loop, assign current_node.next to current_node.

Step 13
The while loop you've just created enables you to go through each node in the list until the last node is reached. Once that happens, you can add the node to the list.
In the else block, right after the while block, assign node to current_node.next.

Step 14
After adding a new node to the list, you need to update its length. At the end of the add method, increment self.length by 1.

Step 15
Great! Now let's test adding elements to your linked list. At the bottom of your code, after creating an instance of LinkedList called my_list and printing my_list.is_empty(), add 1 and 2 to the list using the add method.
Then, print my_list.is_empty() again to confirm that the list is no longer empty. Finally, print my_list.length to see the current length of the linked list.

Step 16
Next, you're going to create another method that will be used to remove a given element from the linked list.
Create a method called remove with two parameters, self and element. Inside it, create a variable called previous_node and assign None to it.

Step 17
Inside the remove method, create a variable named current_node and assign it the value of self.head.
This starts the traversal of the linked list from the first node. current_node will be used to keep track of the node currently being examined as you look for the node containing the specified element to remove.

Step 18
Next, you'll loop through the linked list to find the node that contains the specified element to remove.
Create a while loop that checks when current_node is not None and when current_node.element is not equal to element. Inside the while loop, assign current_node to previous_node.

Step 19
Next, assign current_node.next to current_node in the while loop.
This moves the current_node pointer to the next node in the list during each iteration of the loop, allowing you to traverse the linked list until the element is found or the end of the list is reached.

Step 20
After the while loop, create an if statement that checks if current_node is None.
When this happens, the linked list has been traversed without finding the element to remove and the function should stop running. Therefore, add the return keyword inside the if body.

Step 21
Next, create an elif statement that checks that previous_node is not None. Assign current_node.next to previous_node.next inside it.
With that, if the element to be removed is found and it's not in the head node, the next pointer of the previous node will be updated to skip over the current node (the element to be removed), removing it from the linked list.

Step 22
Next, create an else block that assigns current_node.next to self.head.
This handles the case where the element to be removed is found in the head node. By updating self.head to point to current_node.next, the head node is removed from the linked list.

Step 23
Next, at the end of the remove method, decrement self.length by 1. This decreases the length of the linked list to reflect the removal of a node.

Step 24
Now, let's test removing an element from your linked list. At the bottom of your code, remove 1 from the list using the remove method. Then, print my_list.length again to see the updated length of the linked list.
With that, the linked list data structure workshop is complete!
"""

class LinkedList:
    class Node:
        def __init__(self, element):
            self.element = element
            self.next = None
            
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0
    
    def add(self, element):
        node = self.Node(element)

        if self.is_empty():
            self.head = node
        else:
            current_node = self.head

            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = node
    
        self.length += 1

    def remove(self, element):
        previous_node = None
        current_node = self.head

        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return
        elif previous_node is not None:
            previous_node.next = current_node.next
        else:
            self.head = current_node.next

        self.length -= 1
    
my_list = LinkedList()
print(my_list.is_empty())

my_list.add(1)
my_list.add(2)

print(my_list.is_empty())
print(my_list.length)

my_list.remove(1)
print(my_list.length)