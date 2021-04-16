class SnapshotArray:
    def __init__(self, length: int):
        self.cache = [[[-1, 0]] for _ in range(length)]
        self.sid = 0

    def set(self, index: int, val: int) -> None:
        self.cache[index].append([self.sid, val])

    def snap(self) -> int:
        self.sid += 1
        return self.sid - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect(self.cache[index], [snap_id + 1]) - 1
        return self.cache[index][i][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)