def func(arr, n):
    min_plate_position = arr.index(min(arr))
    max_plate_position = arr.index(max(arr))

    return (
        min_plate_position
        + (n - 1 - max_plate_position)
        + (-1 if min_plate_position > max_plate_position else 0)
    )


print(func([2, 4, 3, 1, 6], 5))
print(func([4, 11, 9, 10, 12], 5))
