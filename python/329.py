from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        maxL = 0
        m, n = len(matrix), len(matrix[0])
        memo = [[0 for i in range(n)] for j in range(m)]

        def dfs(i, j, m, n):
            if memo[i][j] > 0:
                return memo[i][j]
            local_max = 0
            for k in dirs:
                x, y = i + k[0], j + k[1]
                if x >= 0 and y >= 0 and x < m and y < n and matrix[i][j] < matrix[x][y]:
                    local_max = max(local_max, dfs(x, y, m, n))
            memo[i][j] = local_max + 1

            return memo[i][j]

        for i in range(m):
            for j in range(n):
                maxL = max(maxL, dfs(i, j, m, n))

        return maxL
