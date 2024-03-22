'''
- Link to Problem: https://leetcode.com/problems/merge-two-sorted-lists/
- Time Complexity: O(N + M)
- Space Complexity: O(1)
'''

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional['ListNode'], list2: Optional['ListNode']) -> Optional['ListNode']:
        
        result = temp = ListNode()
        
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                temp = temp.next
                list1 = list1.next
                temp.next = None
            else:
                temp.next = list2
                temp = temp.next
                list2 = list2.next
                temp.next = None
        
        if list1:
            temp.next = list1
        elif list2:
            temp.next = list2
        return result.next
    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next