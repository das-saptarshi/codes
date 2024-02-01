'''
- Link to Problem: https://www.geeksforgeeks.org/problems/trie-insert-and-search0651/1
- Time Complexity: 
            1. Insert: O(N) [N = len of key]
            2. Search: O(N) [N = len of key]
- Space Complexity: O(26 * K) [K = len of longest key]
'''



class TrieNode: 
    def __init__(self): 
        self.children = [None]*26  
        self.isEndOfWord = False


class Solution:
    def insert(self, root: TrieNode, key: str):        
        for x in key:
            index = ord(x) - ord('a')
            if root.children[index] == None:
                root.children[index] = TrieNode()
            root = root.children[index]
        
        root.isEndOfWord = True
    
    def search(self, root: TrieNode, key: str):
        
        for x in key:
            index = ord(x) - ord('a')
            if root.children[index] == None:
                return False
            root = root.children[index]
        
        return root.isEndOfWord