# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nthToTail(self, node):
        if node.next!=None:
            return self.nthToTail(node.next)+1
        else:
            return 1
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        print(head)
        size  = self.nthToTail(head)
        if size == n:
            return head.next
        p = head
        for i in range(size, n+1, -1):
            p = p.next
            print("p is {}".format(p.val))
        p.next = p.next.next
        return head

            
        
