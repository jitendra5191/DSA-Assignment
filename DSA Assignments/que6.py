"""
Question 6: Reverse Linked List

Given the head of a singly linked list, reverse the list and return the
reversed list.
"""


class ListNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.next = None


def reverse_list(head: ListNode) -> ListNode:
    prev = None
    curr = head

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


def build_list(values: list[int]) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def print_list(head: ListNode) -> str:
    nodes = []
    curr = head
    while curr:
        nodes.append(str(curr.val))
        curr = curr.next
    return "[" + " -> ".join(nodes) + "]"


if __name__ == "__main__":
    head1 = build_list([1, 2, 3, 4, 5])
    print(f"Input : {print_list(head1)}")
    head1 = reverse_list(head1)
    print(f"Output: {print_list(head1)}")

    head2 = build_list([1, 2])
    print(f"\nInput : {print_list(head2)}")
    head2 = reverse_list(head2)
    print(f"Output: {print_list(head2)}")

    head3 = build_list([42])
    print(f"\nInput : {print_list(head3)}")
    head3 = reverse_list(head3)
    print(f"Output: {print_list(head3)}")

    head4 = build_list([])
    print(f"\nInput : {print_list(head4)}")
    head4 = reverse_list(head4)
    print(f"Output: {print_list(head4)}")
