'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/print-common-nodes-in-bst/1
- Time Complexity: O(N + M) [N: number of nodes in Tree 1, M: number of nodes in Tree 2]
- Space Complexity: O(N + M)
'''

from typing import List

class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Node = None
        self.right: Node = None

class Solution:
    def findCommon(self, root1: Node, root2: Node) -> List[int]:
        return self.findCommonElements(
                self.inorderTraversal(root1),
                self.inorderTraversal(root2)
            )
    
    def inorderTraversal(self, root: Node) -> List[int]:
        if not root:
            return []
        
        return self.inorderTraversal(root.left) + [root.data] + self.inorderTraversal(root.right)
    
    def findCommonElements(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        index1 = index2 = 0
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] == nums2[index2]:
                result.append(nums1[index1])
                index1 += 1
                index2 += 1
            elif nums1[index1] < nums2[index2]:
                index1 += 1
            else:
                index2 += 1
        
        return result