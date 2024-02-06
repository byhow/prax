def getMinimumDistance(center: [int], destination: [int]):
    center.sort()
    destination.sort()

    min_lag = 0
    for i in range(len(center)):
        min_lag += abs(center[i] - destination[i])

    return min_lag
