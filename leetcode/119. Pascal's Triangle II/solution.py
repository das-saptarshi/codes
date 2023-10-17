'''
- Link to Problem: https://leetcode.com/problems/pascals-triangle-ii/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for _ in range(rowIndex):
            temp = [1]
            for j in range(1,len(ans)):
                temp.append(ans[j-1]+ans[j])
            temp.append(1)
            ans = temp [:]
        return ans