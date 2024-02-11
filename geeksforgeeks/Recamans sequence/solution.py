'''
- Link to Problem: https://www.geeksforgeeks.org/problems/recamans-sequence4856/1
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

class Solution:
    def recamanSequence(self, n):
        sequence = [0]
        unique = {0, }
        
        for turn in range(1, n + 1):
            value = sequence[-1] - turn
            if value > 0 and not value in unique:
                sequence.append(value)
            else:
                sequence.append(sequence[-1] + turn)
        
            unique.add(sequence[-1])
        return sequence