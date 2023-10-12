
'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/nodes-at-given-distance-in-binary-tree/1
- Time Complexity: O(NLogN)
- Space Complexity: O(N)
'''


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def KDistanceNodes(self, root: Node, target: int, k: int):
        self.ans = []
        self.findTarget(root, target, k)
        
        return sorted(self.ans)
    
    def findTarget(self, root: Node, target: int, k: int):
        if not root: return 0
        
        if root.data == target:
            self.findNodesAtDistanceK(root.left, k - 1)
            self.findNodesAtDistanceK(root.right, k - 1)
            return 1
        
        dist = self.findTarget(root.left, target, k)
        if dist > 0:
            x = k - dist
            if x == 0: self.ans.append(root.data)
            self.findNodesAtDistanceK(root.right, x - 1)
            return dist + 1
        
        dist = self.findTarget(root.right, target, k)
        if dist > 0:
            x = k - dist
            if x == 0: self.ans.append(root.data)
            self.findNodesAtDistanceK(root.left, x - 1)
            return dist + 1
        
        return 0
        
    
    def findNodesAtDistanceK(self, root: Node, k: int):
        if not root or k < 0:
            return 
            
        if k == 0:
            self.ans.append(root.data)
            return
        
        self.findNodesAtDistanceK(root.left, k - 1)
        self.findNodesAtDistanceK(root.right, k - 1)