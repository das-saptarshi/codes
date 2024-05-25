'''
- Link to Problem: https://leetcode.com/problems/maximum-score-words-formed-by-letters/
- Time Complexity: O(2ᵂ (L + A)) [W = number of words, L = max length of a word, A = number of alphabets]
- Space Complexity: O(A)
'''

from typing import List, Dict
from collections import Counter

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        scores = self.buildScores(letters, score)

        def maxScore(index):
            if index == len(words):
                return 0
            
            word = words[index]
            ans = maxScore(index + 1)

            if self.isWordPossible(word, scores):
                score = self.addWord(word, scores)
                ans = max(ans, maxScore(index + 1) + score)
                self.removeWord(word, scores)

            return ans 
        
        return maxScore(0)

    
    def isWordPossible(self, word: str, scores: Dict[str, 'Score']) -> bool:
        return all(scores.get(letter, Score()).hasMore(count) for letter, count in Counter(word).items())

    def buildScores(self, letters: List[str], scores: List[int]) -> Dict[str, 'Score']:
        return {letter: Score(count, scores[ord(letter) - ord('a')]) for letter, count in Counter(letters).items()}
    
    def addWord(self, word: str, scores: Dict[str, 'Score']) -> int:
        return sum(scores[letter].take() for letter in word)

    def removeWord(self, word: str, scores: Dict[str, 'Score']) -> None:
        for letter in word:
            scores[letter].give()

class Score:
    def __init__(self, count: int = 0, score: int = 0) -> None:
        self.count = count
        self.score = score

    def __str__(self) -> str:
        return f'{self.count} {self.score}'

    def take(self):
        self.count -= 1
        return self.score

    def give(self):
        self.count += 1

    def hasMore(self, count):
        return self.count >= count
        