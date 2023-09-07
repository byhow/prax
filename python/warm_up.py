cars = ["toyota"]
for i in cars:
    if i == "toyota":
        print(f"yes {i}")


from collections import deque

# Initializing a queue
q = deque()

# Adding elements to a queue
q.append("a")
q.append("b")
q.append("c")

print("Initial queue")
print(q)

# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.pop())
print(q.popleft())
# print(q.popleft())

print("\nQueue after removing elements")
print(q)

# Uncommenting q.popleft()
# will raise an IndexError
# as queue is now empty

stack = []
for i in range(3):
    stack.append(i)

print(f"stack is {stack}")
print(stack.pop())
print(stack.pop(0))

print(f"stack looks like this right now: {stack}")


class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None


n = Node(1)
n.next = Node(2)
l = LinkedList()
l.head = n
print(l)

from collections import defaultdict

a = defaultdict()
a["a"] = 1
print(a)
