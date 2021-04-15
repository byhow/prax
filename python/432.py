



class Node(object):
    def __init__(self):
        self.keys = set()
        self.prev, self.next = None, None
    
    def add_key(self, k):
        self.keys.add(k)
    
    def remove_key(self, k):
        self.keys.remove(k)
        
    def get_key(self):
        if self.keys:
            res = self.keys.pop()
            self.add_key(res)
            return res
        else:
            return None
    
    def count(self):
        return len(self.keys)
    
    def is_empty(self):
        return len(self.keys) == 0
    
class DoubleLinkedList(object):
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.next = self.tail, self.head
    
    def append(self, x):
        node, temp = Node(), x.next
        x.next, node.prev = node, x
        node.next, temp.prev = temp, node
        return node
    
    def prepend(self, x):
        return self.append(x.prev)
    
    def remove(self, x):
        prev = x.prev
        prev.next, x.next.prev = x.next, prev
    
    def get_head(self):
        return self.head.next
    
    def get_tail(self):
        return self.tail.prev
    
    def get_sentinel_head(self):
        return self.head
    
    def get_sentinel_tail(self):
        return self.tail
    
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dl, self.counters = DoubleLinkedList(), defaultdict(int)
        self.frequency_map = {0:self.dl.get_sentinel_head()}
        

    def remove_key(self, present_frequency, k):
        node = self.frequency_map[present_frequency]
        node.remove_key(k)
        if node.is_empty():
            self.dl.remove(node)
            self.frequency_map.pop(present_frequency)
        
    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        self.counters[key] += 1
        cur, present_frequency = self.counters[key], self.counters[key] - 1
        if cur not in self.frequency_map:
            self.frequency_map[cur] = self.dl.append(self.frequency_map[present_frequency])
        self.frequency_map[cur].add_key(key)
        if present_frequency > 0:
            self.remove_key(present_frequency, key)
        

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.counters:
            self.counters[key] -=1
            cur, pres = self.counters[key], self.counters[key] +1
            if self.counters[key] == 0:
                self.counters.pop(key)
            if cur != 0:
                if cur not in self.frequency_map:
                    self.frequency_map[cur] = self.dl.prepend(self.frequency_map[pres])
                self.frequency_map[cur].add_key(key)
            self.remove_key(pres, key)
        

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return self.dl.get_tail().get_key() if self.dl.get_tail() and self.dl.get_tail().count() > 0 else ""

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return self.dl.get_head().get_key() if self.dl.get_head() and self.dl.get_head().count()> 0 else ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()