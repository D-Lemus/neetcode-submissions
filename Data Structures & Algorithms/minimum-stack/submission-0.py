class MinStack:

    def __init__(self):
        self.stack = []
        self.min_array = []


    def push(self, val: int) -> None: 
        self.stack.append(val)
        
        if len(self.min_array) == 0:
            self.min_array.append(val)
        else:
            self.min_array.append(min(val,self.min_array[-1]))

    def pop(self) -> None:
        self.stack = self.stack[:-1:]
        self.min_array = self.min_array[:-1:]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_array[-1]
        
