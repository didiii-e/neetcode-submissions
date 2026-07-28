class MinStack:

    def __init__(self):
        self.minstack = []
        self.stack = []
        

    def push(self, val: int) -> None:
        
        if self.stack and val > self.minstack[-1]:
            self.minstack.append(self.minstack[-1])
        else:
            self.minstack.append(val)
        
        self.stack.append(val)

    def pop(self) -> None:
        if self:
            self.stack.pop()
            self.minstack.pop()
        else:
            print('Stack empty -- no value to pop')
        

    def top(self) -> int:
        if self:
            return self.stack[-1]
        else:
            print('Stack empty -- no top value')
        

    def getMin(self) -> int:
        if self:
            return self.minstack[-1]
        else: 
            print('Stack empty -- no min value')
        
