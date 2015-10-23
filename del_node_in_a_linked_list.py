# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        print "here"
        node.val = node.next.val
        print "here2"
        node.next = node.next.next
            
            
Node1=ListNode("Node1")
Node2=ListNode("Node2")
Node3=ListNode("Node3")
Node4=ListNode("Node4")

Node1.next=Node2
Node2.next=Node3
Node3.next=Node4

print "Before Del"
print Node1.next.val
print Node2.next.val
print Node3.next.val
print "After Del"
Solution().deleteNode(Node2)
print Node1.next.val
print Node2.next.val
print Node3.next.val
