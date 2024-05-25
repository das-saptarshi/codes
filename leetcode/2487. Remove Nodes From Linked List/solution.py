'''
- Link to Problem: https://leetcode.com/problems/remove-nodes-from-linked-list/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import Optional

class Solution:
    def removeNodes(self, head: Optional['ListNode']) -> Optional['ListNode']:
        if not head:
            return None

        next_ = self.removeNodes(head.next)

        if next_ and next_.val > head.val:
            return next_
        
        head.next = next_
        return head


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next