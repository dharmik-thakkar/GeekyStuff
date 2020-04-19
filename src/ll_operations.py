class LLOperations(object):
    """
    static class with operations related to linked list
    """
    @staticmethod
    def find_middle_element(head):
        """
        method to find the middle element of the linked list
        :param: head
        :return: middle_element
        """
        if head is None:
            return None
        curr_node = head
        fast_node = head
        while fast_node is not None and fast_node.next is not None:
            curr_node = curr_node.next
            fast_node = fast_node.next.next

        return curr_node.data

