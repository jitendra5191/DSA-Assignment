"""
Question 2: Linked List Cycle Detection

Given head, the head of a linked list, determine if the linked list has a
cycle in it. Return True if there is a cycle, otherwise False.
"""


class ListNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.next = None


def has_cycle(head: ListNode) -> bool:
    if head is None or head.next is None:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next

    return True


if __name__ == "__main__":
    head1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    head1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    print(f"Test Case 1 (cycle at pos 1): {has_cycle(head1)}")

    head2 = ListNode(1)
    node5 = ListNode(2)
    head2.next = node5
    node5.next = head2
    print(f"Test Case 2 (cycle at pos 0): {has_cycle(head2)}")

    head3 = ListNode(1)
    print(f"Test Case 3 (no cycle):       {has_cycle(head3)}")

    print(f"Test Case 4 (null list):      {has_cycle(None)}")
