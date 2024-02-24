# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mark = 0
        sumnode = ListNode()
        start = sumnode
        
        while l1!= None or l2!=None or mark!=0:
            sumnode.next = ListNode()
            sumnode = sumnode.next
            sumnode.val = sumnode.val+mark
            if l1!=None:
                sumnode.val = sumnode.val+l1.val
                l1 = l1.next
            if l2!=None:
                sumnode.val = sumnode.val+l2.val
                l2 = l2.next
            if sumnode.val >= 10:
                sumnode.val = sumnode.val-10
                mark = True
            else:
                mark = False
        return start.next
