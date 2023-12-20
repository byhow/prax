from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        # visited = set()
        num = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    # visited.add((i, j))
                    q = deque([(i, j)])
                    while q:
                        cx, cy = q.popleft()
                        for x, y in directions:
                            xi, yj = x + cx, y + cy
                            if m > xi >= 0 and n > yj >= 0 and grid[xi][yj] == "1":
                                # visited.add((xi, yj))
                                grid[xi][yj] = 0
                                q.append((xi, yj))
                    num += 1
        return num
