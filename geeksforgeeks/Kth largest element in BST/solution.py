'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/kth-largest-element-in-bst/1
- Time Complexity: O(K)
- Space Complexity: O(1)
'''

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def kthLargest(self,root, k):
        
        def solve(root):
            nonlocal k
            if not root:
                return -1
            
            ans = solve(root.right)
            if ans != -1:
                return ans
            k -= 1
            if k == 0:
                return root.data
            return solve(root.left)
        return solve(root)