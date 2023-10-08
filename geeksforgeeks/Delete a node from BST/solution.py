'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/delete-a-node-from-bst/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

def deleteNode(root, X):
    if not root:
        return None
        
    if X < root.data:
        root.left = deleteNode(root.left, X)
        return root
    elif X > root.data:
        root.right = deleteNode(root.right, X)
        return root
    
    if root.left == None:
        return root.right
    elif root.right == None:
        return root.left
    
    predParent = root
    pred = root.left
    
    while pred.right:
        predParent = pred
        pred = pred.right
    
    
    if predParent != root:
        predParent.right = pred.left
    else:
        predParent.left = pred.left
    
    root.data = pred.data
    
    return root