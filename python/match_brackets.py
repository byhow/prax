# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# input s = '({)}'

# Example 3:

# Input: s = "(]"
# Output: false


def match_paren(str):
    if len(str) == 0:
        return True
    if len(str) % 2 != 0:
        return False

    bracket_map = {"[": "]", "{": "}", "(": ")"}
    stack = []
    # ']', '}', ')'

    # stack = ['(', '{', '[', ']', '}', ')']
    # stack = ['(', '{', '}', '[', ']', ')']
    for i in str:
        if i in bracket_map and bracket_map[i]:
            stack.append(bracket_map[i])
        else:
            curr = stack.pop()
            if curr != i:
                return False

    return True


print(match_paren("()"))
print(match_paren("()[]{}"))
print(match_paren("({)}"))
print(match_paren("(]"))
print(match_paren("("))
