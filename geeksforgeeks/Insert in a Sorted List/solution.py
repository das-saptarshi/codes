'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/insert-in-a-sorted-list/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Node = None

class Solution:
    def sortedInsert(self, head: Node, key: int):
        curr = head
        node = Node(key)
        prev = None
        while curr and curr.data < key:
            prev = curr
            curr = curr.next
        
        if not prev:
            node.next = head
            return node
        
        node.next = curr
        prev.next = node
        return head