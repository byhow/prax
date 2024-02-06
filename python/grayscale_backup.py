def findMinimumOperations(img: str):
    # cout << solution("00110101") << endl;
    # cout << solution("101011") << endl;
    # 110101 => 101011
    rev = reversed(img)
    i, j = 0, 0
    n = len(img)
    while i < n and j < n:
        if rev[i] == img[j]:
            j += 1
        i += 1

    # If cannot make the string within 3 moves, then return 3
    return n - j if 3 > (n - j) else 3
