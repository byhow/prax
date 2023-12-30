from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # add all locations of gates to a q
        EMPTY = 2147483647
        q = deque()
        m, n = len(rooms), len(rooms[0])
        for row in range(m):
            for col in range(n):
                if rooms[row][col] == 0:
                    # print("add it")
                    q.append([row, col])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        # print(q)
        while q:
            x, y = q.popleft()
            for r, c in directions:
                rx, ry = r + x, c + y
                if rx >= m or rx < 0 or ry >= n or ry < 0 or rooms[rx][ry] != EMPTY:
                    continue
                rooms[rx][ry] = rooms[x][y] + 1
                q.append([rx, ry])

        # bfs all gates locations and update all empty cells to distance
