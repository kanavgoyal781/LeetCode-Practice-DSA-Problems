# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1=""
        str2=""
        curr1=l1
        curr2=l2
        while curr1!=None:
            str1=str1+str(curr1.val)
            curr1=curr1.next
        while curr2!=None:
            str2=str2+str(curr2.val)
            curr2=curr2.next
        num1=int(str1[::-1])
        num2=int(str2[::-1])
        final=num1+num2
        final=str(final)[::-1]
        dummy=ListNode()
        current=dummy
        for i in range(len(final)):
            next_node=ListNode(int(final[i]))
            current.next=next_node
            current=current.next
        head=dummy.next
        return head



