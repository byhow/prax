class CustomStack:
    def __init__(self, maxSize: int):
        self.size = 0
        self.maxSize = maxSize
        self.incArr = []
        self.s = []

    def push(self, x: int) -> None:
        if self.size < self.maxSize:
            self.s.append(x)
            self.incArr.append(0)
            self.size += 1

    def pop(self) -> int:
        if not self.incArr:
            return -1
        if self.size > 1:
            self.incArr[-2] += self.incArr[-1]
        self.size -= 1
        return self.s.pop() + self.incArr.pop()

    def increment(self, k: int, val: int) -> None:
        if self.incArr:
            self.incArr[min(k, self.size) - 1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)