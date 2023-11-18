'''
- Link to Problem: https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''


class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None

class Solution:
    def reverseDLL(self, head: Node) -> Node:
        curr = head
        prev = None
        
        while curr:
            next = curr.next
            curr.next = prev
            curr.prev = next
            prev = curr
            curr = next
        
        return prev