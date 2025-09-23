'''
- Link to Problem: https://leetcode.com/problems/count-elements-with-maximum-frequency/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = maxFreq = 0
        maxFreq = max(counter.values())
        return sum(freq for num, freq in counter.items() if freq == maxFreq)