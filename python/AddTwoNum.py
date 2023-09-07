class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self):
        self.len = 0
        self.carry = False

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode 2, 3, 4
        :type l2: ListNode 4, 0, 1
        :rtype: ListNode
        result should be 6, 3, 5
        """
        head = ListNode(0)
        tmp = head
        p, q = l1, l2
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0

            val = x + y + (1 if self.carry else 0)
            if val >= 10:
                val -= 10
                self.carry = True
            else:
                self.carry = False

            tmp.next = ListNode(val)
            # tmp.val = val
            p = p.next if p else None
            q = q.next if q else None

            tmp = tmp.next

        if self.carry:
            tmp.next = ListNode(1)
        return head.next


def printLs(node):
    if node:
        print(str(node.val) + " -> ")
        printLs(node.next)


node = ListNode(8)
node.next = ListNode(10)
node.next.next = ListNode(4)

node2 = ListNode(4)
node2.next = ListNode(0)
node2.next.next = ListNode(5)


s = Solution()
a = s.addTwoNumbers(node, node2)
printLs(a)
# printLs(node)
# printLs(node2)
