def binarySearch(l, r, arr, x):
    while l <= r:
        mid = l + (r - l) // 2
        print(mid)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1 
        # print(mid)
    return -1

l_1 = list()
for i in range(10):
    l_1.append(i)

print(l_1)
x = 6
y = binarySearch(0, len(l_1) - 1, l_1, x)

print(y)
















# class TreeNode(object):
#     def __init__(self, data):
#         self.val = data
#         self.left = None
#         self.right = None




