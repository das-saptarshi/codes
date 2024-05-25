'''
- Link to Problem: https://leetcode.com/problems/delete-node-in-a-linked-list/
- Time Complexity: O(1)
- Space Complexity: O(1)
'''


class Solution:
    def deleteNode(self, node: 'ListNode'):
        node.val = node.next.val
        node.next = node.next.next

class ListNode:
    def __init__(self, x: int):
        self.val: int = x
        self.next: ListNode = None