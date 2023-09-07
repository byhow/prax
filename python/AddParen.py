def solution(parentheses):
    # Type your solution here
    count_left = 0
    stack = []
    char = ""

    for i in parentheses:
        if i == "(":
            stack.append(i)
            continue
        else:
            try:
                char = stack[0]
                stack.pop(0)
                if char != "(":
                    count_left += 1
            except:
                count_left += 1

    count_right = len(stack)
    parentheses = "(" * count_left + parentheses + ")" * count_right

    return parentheses


print(solution("("))
