'''
- Link to Problem: https://leetcode.com/problems/reverse-linked-list-ii/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right - left <= 0:
            return head
        
        head = ListNode(0, head)

        curr = head
        skip, size = left - 1, right - left + 1

        while skip:
            curr = curr.next
            skip -= 1

        x = curr
        curr = curr.next
        prev = None

        while size > 0:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
            size -= 1
            
        x.next.next = curr
        x.next = prev

        return head.next