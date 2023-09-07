def sortf(elem):
    return elem[2]


def bestPros2(pros, k):
    # ret = []
    pro_length = len(pros)
    min_score, index = pros[0][0], 0
    # min_set_index = set()

    for i in range(pro_length):
        if min_score > pros[i][0]:
            min_score = pros[i][0]
            index = i

    for j in range(pro_length):
        pros[j].append((pros[j][0] - min_score) * pros[j][1])
        pros[j].append(j)

    # print(pros)

    ret1 = sorted(pros, key=sortf)
    ret = []
    for i in range(pro_length):
        if i > k - 1:
            break
        else:
            ret.append(ret1[i][-1])
    return ret

    # ret.append(index)
    # print(ret)
    # min_set_index.add(index)
    # print(min_score)

    # for i in range(k - 1):
    #     _min = math.inf
    #     for j in range(pro_length):
    #         # print((pros[j][0] - min_score) * pros[j][1], j)
    #         # print(min_set_index)
    #         if (pros[j][0] - min_score) * pros[j][1] < _min and (j not in min_set_index):
    #             # print(j, min_set_index)
    #             _min = (pros[j][0] - min_score) * pros[j][1]
    #             index = j
    #     # print(min_set_index)
    #     min_set_index.add(index)
    #     ret.append(index)


print(bestPros2([[5, 4], [4, 3], [6, 5], [3, 5]], 2))
