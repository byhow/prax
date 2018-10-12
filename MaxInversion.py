# Complete the maxInversions function below.
def maxInversions(prices):
    count = 0
    for i in range(1, len(prices) - 1):
        less_num = 0
        greater_num = 0
        for j in range(i + 1, len(prices)):
            if prices[j] < prices[i]:
                less_num += 1
                print(less_num)
        for k in range(0, i - 1):
            if prices[k] > prices[i]:
                greater_num += 1
        count += greater_num * less_num    
    return count
