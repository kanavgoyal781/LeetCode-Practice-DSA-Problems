# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow=head
        fast=head
        length=0
        while slow:
            length=length+1
            slow=slow.next
        slow=head
        if length==0:
            return None
        if k>=length:
            k=k%length
        else:
            k=k
        if k==0 or head.next==None:
            return head
        for i in range(k):
            fast=fast.next
        while fast.next:
            fast=fast.next
            slow=slow.next
        changed_head=slow.next
        slow.next=None
        fast.next=head
        return changed_head

        