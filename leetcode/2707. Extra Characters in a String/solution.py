'''
- Link to Problem: https://leetcode.com/problems/extra-characters-in-a-string/
    
    Let N be the number of characters in the string 's'.
    Let M be the average size of a word in 'dictonary'.
    Let K be the number of words in 'dictionary'.

- Time Complexity: O(N**2 + M*K) [N**2 for dp traversing and M*K for building the Trie]
- Space Complexity: O(N + M*K) [N for dp and M*K for Trie]
'''


from typing import List
from collections import defaultdict

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        root = self.buildTrie(dictionary)
        
        dp = [0] * (n + 1)
        for start in range(n - 1, -1, -1):
            dp[start] = dp[start + 1] + 1

            curr = root
            for end in range(start, n):
                if s[end] not in curr.children:
                    break
                curr = curr.children[s[end]]
                if curr.isWord:
                    dp[start] = min(dp[start], dp[end + 1])
        return dp[0]
    
    def buildTrie(self, words):
        root = TrieNode()

        for word in words:
            curr = root
            for x in word:
                curr = curr.children[x]
            curr.isWord = True
        return root
        

class TrieNode:
    def __init__(self):
        self.children = defaultdict(lambda: TrieNode())
        self.isWord = False