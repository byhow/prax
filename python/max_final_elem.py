# Given an array arr[] consisting of N integers, rearrange the array such that it satisfies the following conditions:

# arr[0] must be 1.
# Difference between adjacent array elements should not exceed 1, that is, arr[i] – arr[i-1] <= 1 for all 1 <= i < N.
# The permissible operations are as follows:

# Rearrange the elements in any way.
# Reduce any element to any number >= 1.
# The task is to find the maximum possible value that can be placed at the last index of the array.


def max_final_elem(arr: [int]):
    arr.sort()
    if arr[0] != 1:
        arr[0] = 1

    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] > 1:
            arr[i] = arr[i - 1] + 1

    return arr[-1]
