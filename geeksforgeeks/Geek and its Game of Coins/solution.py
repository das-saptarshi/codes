'''
- Link to Problem: https://www.geeksforgeeks.org/problems/geek-and-its-game-of-coins4043/1
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

class Solution:
    def findWinner(self, n : int, x : int, y : int) -> int:
        geek_wins = [False] * (n + 1)
        
        for i in range(1, n + 1):
            
            if not geek_wins[i - 1]:
                geek_wins[i] = True
            elif i - x >= 0 and not geek_wins[i - x]:
                geek_wins[i] = True
            elif i - y >= 0 and not geek_wins[i - y]:
                geek_wins[i] = True
        
        return int(geek_wins[n])