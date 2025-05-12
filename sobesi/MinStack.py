class MinStack:
    def __init__(self, data: tuple = ()):
        self.data = data

    def push(self, val: int) -> None:
        self.data += (val,)

    def pop(self) -> None:
        self.data = self.data[:-1]

    def top(self) -> int:
        return self.data[-1] if len(self.data) > 0 else None

    def getMin(self) -> int:
        return min(self.data)


min_stack = MinStack()

min_stack.push(3)
min_stack.push(4)
min_stack.push(5)

min_stack.pop()
print(min_stack.top())
print(min_stack.getMin())
