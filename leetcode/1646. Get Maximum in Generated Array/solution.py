# Link to Problem: https://leetcode.com/problems/get-maximum-in-generated-array/description/
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 0:
            return 0
        nums = [0, 1]

        for i in range(1, n):
            nums.append(nums[i])
            if (2 * i + 1) <= n:
                nums.append(nums[i] + nums[i + 1])
                
        return max(nums)