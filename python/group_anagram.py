from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we can use count map
        cmap = defaultdict(list)

        for s in strs:
            alpha_bitmap = [0] * 26
            for c in s:
                alpha_bitmap[ord(c) - ord("a")] += 1
            cmap[tuple(alpha_bitmap)].append(s)

        return cmap.values()
