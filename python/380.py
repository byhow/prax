class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.idxlist, self.cache = [], {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.cache:
            self.idxlist.append(val)
            self.cache[val] = len(self.idxlist) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.cache:
            idx, last = self.cache[val], self.idxlist[-1]
            self.idxlist[idx], self.cache[last] = last, idx
            self.idxlist.pop()
            self.cache.pop(val, 0)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.idxlist)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()