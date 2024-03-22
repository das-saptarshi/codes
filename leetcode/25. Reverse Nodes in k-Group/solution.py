'''
- Link to Problem: https://leetcode.com/problems/reverse-nodes-in-k-group/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import Optional

class Solution:
    def reverseKGroup(self, head: Optional['ListNode'], k: int, prev: Optional['ListNode'] = None) -> Optional['ListNode']:
        count = 0
        curr = head

        while curr and count < k:
            curr = curr.next
            count += 1
        
        if count != k: return head
        
        curr = head

        while count > 0:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
            count -= 1
        
        head.next = self.reverseKGroup(curr, k, prev)

        return prev

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next