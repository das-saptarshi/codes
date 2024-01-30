'''
- Link to Problem: https://leetcode.com/problems/implement-queue-using-stacks/
- Time Complexity:
            1. Push: O(1)
            2. Pop: O(N)
            3. Peek: O(1)
            4. Empty: O(1)
- Space Complexity: O(N)
'''

class MyQueue:

    def __init__(self):
        self.stack = []
        self.top = None

    def push(self, x: int) -> None:
        if not self.stack:
            self.top = x
        
        self.stack.append(x)

    def pop(self) -> int:
        tempStack = []
        
        while self.stack:
            tempStack.append(self.stack.pop())
        
        x = tempStack.pop()
        if tempStack:
            self.top = tempStack[-1]
        else:
            self.top = None
        
        while tempStack:
            self.stack.append(tempStack.pop())
        return x
    

    def peek(self) -> int:
        return self.top
    

    def empty(self) -> bool:
        return len(self.stack) == 0