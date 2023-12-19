from collections import deque


class Node:
    def __init__(self) -> None:
        self.val = 0
        self.neighbors: [Node] = []


def bfs(root: Node, target: Node):
    q = deque([root])
    step = 0

    while q:
        size = len(q)

        for i in range(size):
            curr: Node = q.popleft()
            if curr == target:
                return step
            q.extend(curr.neighbors)
        step += 1
    return -1
