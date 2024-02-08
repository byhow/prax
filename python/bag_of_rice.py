def perfect_rice_bags(bags):
    bags.sort()
    dp = [0] * (10**6)

    for x in bags:
        dp[x] = 1

    res = -1
    for i in range(len(bags) - 1, -1, -1):
        sq = bags[i] * bags[i]
        dp[bags[i]] += dp[sq]
        res = max(res, dp[bags[i]])
        print(sq)

    return -1 if res < 2 else res


print(perfect_rice_bags([625, 4, 2, 5, 25]))


def maxSetSize(riceBags):
    bag_list = sorted(riceBags)
    max_len = -1

    for i in range(len(bag_list)):
        number = bag_list[i]
        rice_set = [number]
        for j in range(i + 1, len(bag_list)):
            if number * number == bag_list[j]:

                rice_set.append(bag_list[j])
                number = bag_list[j]
        if len(rice_set) < 2:
            continue
        if len(rice_set) > max_len:
            max_len = len(rice_set)

    return max_len
