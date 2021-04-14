class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.cache = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.arr.append(val)
        self.cache[val].add(len(self.arr) - 1)
        return len(self.cache[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if self.cache[val]:
            last, idx = self.arr[-1], self.cache[val].pop()
            self.arr[idx] = last
            if self.cache[last]:
                self.cache[last].add(idx)
                self.cache[last].discard(len(self.arr) - 1)
            self.arr.pop()
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()