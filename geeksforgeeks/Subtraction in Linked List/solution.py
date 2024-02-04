'''
- Link to Problem: https://www.geeksforgeeks.org/problems/subtraction-in-linked-list/1
- Time Complexity:
            1. Remove Extra Zeros: O(N)
            2. Get Greater And Smaller Number: O(N + M)
            3. Length: O(N)
            4. Reverse: O(N)
            5. Subtract: O(Max(N, M))

            Overall: O(N + M)

- Space Complexity: O(1)
'''

from typing import Tuple

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Node = None

class Solution:
    def subLinkedList(self, head1: Node, head2: Node) -> Node: 
        head1, head2 = self.removeExtraZeros(head1), self.removeExtraZeros(head2)
        head1, head2 = self.getGreaterAndSmallerNumber(head1, head2)
        return self.subtract(head1, head2)
    
    def removeExtraZeros(self, head: Node) -> Node:
        while head and head.data == 0:
            head = head.next
        
        if not head:
            return Node(0)
        
        return head
    
    def getGreaterAndSmallerNumber(self, head1: Node, head2: Node) -> Tuple[Node, Node]:
        length1, length2 = self.length(head1), self.length(head2)
        
        if (length1 > length2): return head1, head2
        if (length1 < length2): return head2, head1
        
        while head1 and head2 and head1.data == head2.data:
            head1 = head1.next
            head2 = head2.next
        
        if head1 == None: return Node(0), Node(0)
        
        if head1.data > head2.data: return head1, head2
        return head2, head1
        
    def length(self, head: Node) -> int:
        length = 0
        
        while head:
            length += 1
            head = head.next
        
        return length
        
    
    def reverse(self, head: Node) -> Node:
        if not head: return head
        
        prev = None
        
        while head:
            next_ = head.next
            head.next = prev
            prev = head
            head = next_
        
        return prev
    
    def subtract(self, head1: Node, head2: Node) -> Node:
        head1 = self.reverse(head1)
        head2 = self.reverse(head2)
        head = None
        
        while head1:
            less = 0
            if head2:
                less = head2.data
                head2 = head2.next
                
            if head1.data < less:
                head1.next.data -= 1
                head1.data += 10
            
            node = Node(head1.data - less)
            node.next = head
            head = node
            
            head1 = head1.next
        
        return self.removeExtraZeros(head)