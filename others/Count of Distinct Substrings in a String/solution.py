'''
- Link to Problem: 
- Time Complexity: O(N^2)
- Space Complexity: O(N)
'''


from collections import defaultdict

class Solution:

    def countOfDistinctSubstrings(self, s: str) -> int:
        distinctSubstrings = 1
        trie = Trie()
        
        for i in range(len(s)):
            distinctSubstrings += trie.insertAndCount(s[i:])
        
        return distinctSubstrings
    

class Trie:
    def __init__(self) -> None:
        self.root = Node()
    
    def insertAndCount(self, word: str):
        root = self.root
        count = 0
        for x in word:
            if x not in root.next:
                count += 1
            root = root.next[x]
        return count

class Node:
    def __init__(self) -> None:
        self.next = defaultdict(Node)