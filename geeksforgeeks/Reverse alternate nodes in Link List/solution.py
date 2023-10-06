'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/given-a-linked-list-reverse-alternate-nodes-and-append-at-the-end/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Solution:
    def rearrange(self, head: Node):
        curr = prev = head
        reverse = None
        
        while curr:
            prev = curr
            forward, curr = self.forward(curr)
            reverse = self.reverse(reverse, forward)
        
        prev.next = reverse
        return head
    
    def reverse(self, head: Node, node: Node):
        if head == None:
            return node
        elif node == None:
            return head
        node.next = head
        return node
    
    def forward(self, head: Node):
        if head.next == None:
            return None, None
        forward = head.next
        head.next = forward.next
        forward.next = None
        return forward, head.next