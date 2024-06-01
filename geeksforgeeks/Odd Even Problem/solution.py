'''
- Link to Problem: https://www.geeksforgeeks.org/problems/help-nobita0532/1
- Time Complexity: O(N)
- Space Complexity: O(26)
'''

from collections import Counter

class Solution:
    def oddEven(self, s : str) -> str:
        counter = Counter(s)
        score = 0
        
        for i in range(0, 26, 2):
            x = chr(ord('a') + i)
            y = chr(ord('a') + i + 1)
            
            if x in counter and counter[x] % 2 == 1:
                score += 1
            if y in counter and counter[y] % 2 == 0:
                score += 1
        
        return 'ODD' if score % 2 == 1 else 'EVEN'