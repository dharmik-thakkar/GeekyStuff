from src.data_structures.nodes import Node


class LinkedList(object):
    """
    Class representing a linked list.
    """
    def __init__(self, key=None):
        if key:
            self.head = Node(key)
        else:
            self.head = None

    def traverse(self):
        """
        method to traverse a linked list
        """
        curr_node = self.head
        while curr_node:
            print(" {} ".format(curr_node.data)),
            curr_node = curr_node.next

    def push(self, key):
        """
        method to insert new node at the beginning of linked list
        """
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, key):
        """
        method to insert new node after given node of linked list
        """
        if prev_node is None:
            raise Exception("The prev_node cannot be None.")

        new_node = Node(key)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_after(self, prev_key, key):
        """
        method to insert new node after given key of linked list
        """
        if prev_key is None:
            raise Exception("The prev_key cannot be None.")

        curr_node = self.head
        while curr_node:
            if curr_node.data == prev_key:
                break
            curr_node = curr_node.next

        if curr_node:
            new_node = Node(key)
            new_node.next = curr_node.next
            curr_node.next = new_node
        else:
            raise Exception("Couldn't find the given prev_key. Skipping insertion.")

    def append(self, key):
        """
        method to insert new node at the end of the list
        """
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
