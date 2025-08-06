# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Compute the length of the list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Step 2: Handle deletion of head
        pos = length - n
        if pos == 0:
            return head.next

        # Step 3: Walk to (pos - 1)th node
        current = head
        for _ in range(pos - 1):
            current = current.next

        # Step 4: Skip the nth node from end
        if current.next:
            current.next = current.next.next

        return head