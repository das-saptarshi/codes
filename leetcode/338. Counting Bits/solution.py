# Link to Problem: https://leetcode.com/problems/counting-bits/
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0, 1]

        if n <= 1:
            return ans[: n + 1]
        target = n + 1

        while True:
            mid = len(ans) // 2
            end = len(ans)

            for i in range(mid, end):
                ans.append(ans[i])
                ans.append(ans[i] + 1)       

                if len(ans) >= target:
                    return ans[:  target]