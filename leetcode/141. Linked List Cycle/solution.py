'''
- Link to Problem: https://leetcode.com/problems/linked-list-cycle/
- Time Complexity: O(n)
- Space Complexity: O(1)
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
            
        slow, fast = head, head.next

        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next
            if slow == fast:
                return True
        
        return False
        