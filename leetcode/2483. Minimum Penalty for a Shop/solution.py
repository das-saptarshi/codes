# Link to Problem: https://leetcode.com/problems/minimum-penalty-for-a-shop/
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        openPenalties, closePenalties = 0, customers.count('Y')
        
        index, minValue = 0, closePenalties
        for i in range(n):
            if customers[i] == 'Y':
                closePenalties -= 1
            else:
                openPenalties += 1
            
            if (openPenalties + closePenalties) < minValue:
                minValue = openPenalties + closePenalties
                index = i + 1
        
        return index