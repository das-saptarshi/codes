'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1
- Time Complexity: O(N + M) [N, M: length of LinkedList first and second respectively]
- Space Complexity: O(N + M)
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def addTwoLists(self, first: Node, second: Node):
        first = self.reverse(first)
        second = self.reverse(second)
        carry = 0
        result = curr = Node(0)
        
        while first and second:
            x = first.data + second.data + carry
            first, second = first.next, second.next
            curr, carry = self.addNum(curr, x)
        
        while first:
            x = first.data + carry
            first = first.next
            curr, carry = self.addNum(curr, x)
        
        while second:
            x = second.data + carry
            second = second.next
            curr, carry = self.addNum(curr, x)
        
        if carry:
            self.addNum(curr, carry)
        
        return self.reverse(result.next)
            
    def addNum(self, head: Node, x: int):
        carry, num = divmod(x, 10)
        head.next = Node(num)
        
        return head.next, carry
    
    def reverse(self, head: Node):
        prev = None
        curr = head
        
        while curr:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        
        return prev