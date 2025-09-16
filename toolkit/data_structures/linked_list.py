'''A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.
It consists of nodes where each node contains a data field and a reference(link) to the next node in the list.
''' 

class Node:
    # Represents a single node in a linked list.
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Represents a singly linked list.
    def __init__(self):
        self.head = None

    def append(self, data):
        # Appends a new node with the given data to the end of the list.
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def __str__(self):
        # Returns a string representation of the linked list.
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(str(current_node.data))
            current_node = current_node.next
        return " -> ".join(nodes) + " -> None"