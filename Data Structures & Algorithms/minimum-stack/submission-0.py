class MinStack:
    """
    1, 2, 0, 4, 3, -1, 
                i
 
    stack = [1, 2, -1]
    mins =  [1, -1]

    edge case: duplicate values
    """

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        num = self.stack.pop()
        if num == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        
