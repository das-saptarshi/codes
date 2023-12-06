'''
- Link to Problem: https://leetcode.com/problems/calculate-money-in-leetcode-bank/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Solution:
    def totalMoney(self, n: int) -> int:

        money = 0
        start = 1
        while n > 0:
            dayMoney = start
            for _ in range(min(7, n)):
                money += dayMoney
                dayMoney += 1
            start += 1
            n -= 7
        
        return money