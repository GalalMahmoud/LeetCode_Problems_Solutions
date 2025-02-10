class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if not len(self.min_stack):
            self.min_stack.append(val)
        elif self.min_stack[-1] >= val: self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack):
            if self.stack[-1] == self.min_stack[-1]: self.min_stack = self.min_stack[:-1]
            self.stack = self.stack[:-1]
        return None

    def top(self) -> int:
        if len(self.stack):
            return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]