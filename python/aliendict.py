class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordmap = {}
        for i in range(len(order)):
            ordmap[order[i]] = i
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                if words[i][j] != words[i + 1][j]:
                    if ordmap[words[i][j]] > ordmap[words[i + 1][j]]:
                        return False
                    break

        return True
