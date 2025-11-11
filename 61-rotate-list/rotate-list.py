# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return
        if head.next==None:
            return head
        current=head
        prev=None
        length=0
        while current!=None:
            prev=current
            current=current.next
            length=length+1
        rotation_l=k%length
        if rotation_l==0:
            return head
        current=head
        for i in range(length-rotation_l-1):
            current=current.next
        ans=current.next
        current.next=None
        prev.next=head
        return ans

        



