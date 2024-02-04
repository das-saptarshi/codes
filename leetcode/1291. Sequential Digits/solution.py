'''
- Link to Problem: https://leetcode.com/problems/sequential-digits/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        start = len(str(low))
        end = len(str(high))
        
        numbers = ['1','2','3','4','5','6','7','8','9']
        ans = []
        
        for i in range(start, end+1):
            
            for j in range(10 - i):
                number = int(''.join(numbers[j:j+i]))
                if low <= number <= high:
                    ans.append(number)
                elif number > high:
                    break
        return ans