# Link to Problem: https://leetcode.com/problems/implement-stack-using-queues/
# Time Complexity: 
#   1. push - O(1)
#   2. pop - O(n)
#   3. top - O(n)
#   4. empty - O(1)
# Space Complexity: O(n**2)

class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        for _ in range(len(self.queue) - 1):
            self.push(self.queue.pop(0))
        
        return self.queue.pop(0)

    def top(self) -> int:
        x = self.pop()
        self.push(x)
        return x

    def empty(self) -> bool:
        return not bool(self.queue)