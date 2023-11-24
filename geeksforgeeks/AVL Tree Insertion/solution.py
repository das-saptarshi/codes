'''
- Link to Problem: https://www.geeksforgeeks.org/problems/avl-tree-insertion/1
- Time Complexity: O(LogN)
- Space Complexity: O(1)
'''

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

class Solution:
    def insertToAVL(self, root: Node, key: int) -> Node: 
        if not root: 
            return Node(key) 
        elif key < root.data: 
            root.left = self.insertToAVL(root.left, key) 
        else: 
            root.right = self.insertToAVL(root.right, key) 
  
        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right)) 

        balance = self.getBalance(root) 

        if balance > 1 and key < root.left.data: 
            return self.rightRotate(root) 

        if balance < -1 and key > root.right.data: 
            return self.leftRotate(root) 

        if balance > 1 and key > root.left.data: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 

        if balance < -1 and key < root.right.data: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
  
    def leftRotate(self, z: Node) -> Node:
        y: Node = z.right 
        T2: Node = y.left 

        y.left = z 
        z.right = T2 
        
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 

        return y 
  
    def rightRotate(self, z: Node) -> Node: 
        y: Node = z.left 
        T3: Node = y.right 
   
        y.right = z 
        z.left = T3 
  
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 
  
        return y 
  
    def getHeight(self, root: Node) -> int: 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root: Node) -> int: 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right)