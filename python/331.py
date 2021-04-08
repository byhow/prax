class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        po = preorder.split(",")
        slots = 1
        for i in po:
            if slots == 0:
                return False
            if i == "#":
                slots -= 1
            else:
                slots += 1
        return slots == 0
