def groupStudents(levels: [int], maxSpread: int) -> int:
    i, teams = 1, 0
    levels.sort()
    n = len(levels)
    curr_level = levels[0]
    while i < n:
        if abs(curr_level - levels[i]) > maxSpread:
            teams += 1
            if i + 1 < n:
                curr_level = levels[i + 1]
        i += 1

    return teams


print(groupStudents([1, 4, 7, 3, 4], 2))  # max 3, (1, 3)(4, 4)(7)


# https://leetcode.com/discuss/interview-question/1688196/amazon-online-assessment-maximum-number-of-engineering-teams
def max_eng(team_size, maxdiff, skill):
    i = 0
    teams = 0
    skill.sort()
    while i < len(skill):
        if i + team_size - 1 >= len(skill):
            break
        if skill[i + team_size - 1] - skill[i] > maxdiff:
            i += 1
            continue
        teams += 1
        i += team_size
    return teams
