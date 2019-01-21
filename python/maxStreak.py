def maxStreak(m, data):
    # Write your code here
    ppl = m * 'Y'
    streak = 0
    ret = 0
    for i in data:
        if i == ppl:
            streak += 1
            if ret < streak:
                ret = streak
        else:
            streak = 0

    return ret


if __name__ == '__main__':
    print(maxStreak(4,[1, 2, 3]))
