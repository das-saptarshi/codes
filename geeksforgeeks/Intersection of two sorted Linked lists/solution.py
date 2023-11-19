'''
- Link to Problem: https://www.geeksforgeeks.org/problems/intersection-of-two-sorted-linked-lists/1
- Time Complexity: O(min(H1, H2)) [H1: len of linked list head1, H2: len of linked list H2]
- Space Complexity: O(1)
'''


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class Solution:
    def findIntersection(self, head1: Node, head2: Node) -> Node:
        
        head = curr = Node(0)
        
        while head1 and head2:
            if head1.data == head2.data:
                curr.next = Node(head1.data)
                curr, head1, head2 = curr.next, head1.next, head2.next
            elif head1.data < head2.data:
                head1 = head1.next
            else:
                head2 = head2.next
        
        return head.next