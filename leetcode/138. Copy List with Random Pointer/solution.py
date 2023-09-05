'''
- Link to Problem:https://leetcode.com/problems/copy-list-with-random-pointer/
- Time Complexity: O(N) [N = size of linked list]
- Space Complexity: O(N) [For Map]
'''


from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        nodeMap = {}
        copyList = node = Node(0)
        curr = head

        while curr:
            node.next = Node(curr.val)
            nodeMap[curr] = node = node.next
            curr = curr.next

        node = copyList.next
        curr = head

        while curr:
            node.random = nodeMap.get(curr.random, None)
            curr, node = curr.next, node.next
        
        return copyList.next