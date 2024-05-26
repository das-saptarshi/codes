'''
- Link to Problem: https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import Optional

class Solution:
    def doubleIt(self, head: Optional['ListNode']) -> Optional['ListNode']:
        curr = head

        def reverse(head: 'ListNode'):
            prev = None
            while head:
                next = head.next
                head.next = prev
                prev = head
                head = next
            return prev
        
        curr = head = reverse(head)
        carry = 0
        
        while curr:
            carry, curr.val = divmod(curr.val * 2 + carry, 10)
            if carry > 0 and not curr.next:
                curr.next = ListNode(0)
            curr = curr.next

        return reverse(head)
    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next