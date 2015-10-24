# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
class Solution(object):
    def removeElements(self, head, val):
        self = ListNode(0)
        # self.next = head 
        # head = self
        self.next, head = head, self   

        while head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next

        return self.next

node1=ListNode(1)
node2=ListNode(2)
node1.next=node2
print node1
print node2

print Solution().removeElements(node1,1)
