'''
- Link to Problem: https://leetcode.com/problems/word-break-ii/
- Time Complexity: O(2 ^ S + N * M) [S = length of string s, N = number of words in word_dict, M = avg length of word in word_dict]
- Space Complexity: O(N * M)
'''

from typing import List
from collections import defaultdict

class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> List[str]:
        trie = Trie()

        for word in word_dict:
            trie.add_word(word)
        
        def generate(index, root, words):
            if index == len(s):
                if sum(len(word) for word in words) == len(s):

                    results.append(' '.join(words))
                return
            
            if s[index] not in root.next:
                return 
            
            root = root.next[s[index]]

            generate(index + 1, root, words)
            if root.is_word:
                generate(index + 1, trie.root, words + [root.word])
        
        results = []
        generate(0, trie.root, [])

        return results



class Node:
    def __init__(self):
        self.next = defaultdict(lambda: Node())
        self.is_word = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = Node()
    
    def add_word(self, word: str) -> None:
        root = self.root

        for letter in word:
            root = root.next[letter]
        
        root.is_word = True
        root.word = word