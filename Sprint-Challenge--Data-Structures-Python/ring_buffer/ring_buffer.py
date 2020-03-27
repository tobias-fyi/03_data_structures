from doubly_linked_list import DoublyLinkedList
from typing import Any


class RingBuffer:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item: Any) -> None:
        """Adds an element to the buffer."""
        if len(self.storage) < self.capacity:
            # If buffer is not full, simply add to tail
            self.storage.add_to_tail(item)
            self.current = self.storage.tail  # Update cursor
        else:  # If buffer is full, overwrite next item
            # If cursor is on tail, loop back to head
            if self.current.next is None:
                # Replace head node with new item
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head  # Set cursor to new head
            else:  # If cursor is not at tail, replace next item
                # Uses the ListNode methods (don't update list length)
                self.current.next.delete()  # Remove next item
                # Insert new item after current
                self.current.insert_after(item)
                # Set current to next item
                self.current = self.current.next

    def get(self):
        """Returns all of the elements in the buffer 
        in a list in their given order.
        """
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # Set initial current node
        node = self.storage.head

        # Iterate through DLL, appending values to list in order
        while node:
            if node.value is not None:
                list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents


# ----------------Stretch Goal-------------------
class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
