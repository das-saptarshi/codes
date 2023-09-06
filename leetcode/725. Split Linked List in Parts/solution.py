'''
- Link to Problem: https://leetcode.com/problems/split-linked-list-in-parts/
- Time Complexity:O(N)
- Space Complexity: O(N)
'''

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size = self.size(head)
        n, extra = divmod(size, k)
        result = []
        
        head = self.splitAndAdd(result, head, extra, n + 1)
        head = self.splitAndAdd(result, head, k - extra, n)

        return result

    def splitAndAdd(self, result, head, n, k):
        for i in range(n):
            result.append(head)
            tempK, prev = k, None
            while head and tempK > 0:
                tempK -= 1
                prev, head = head, head.next
            if prev != None:
                prev.next = None
        
        return head

    def size(self, head):
        size = 0
        while head:
            head = head.next
            size += 1
        return size
        