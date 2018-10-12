def prod(m, n):
    if n < 1:
        return 0
    return m + prod(m, n - 1)

print(str(prod(10, 4)))