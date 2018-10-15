# Given a string consisting of the letters ,  and , we can perform the following operation:
# Take any two adjacent distinct characters and replace them with the third character.
# Find the shortest string obtainable through applying this operation repeatedly.
# For example, given the string  we can reduce it to a  character string by replacing  with  and  with : .
# Input Format
# The first line contains the number of test cases .
# Each of the next  lines contains a string  to process.
# Constraints


# Output Format
# For each test case, print the length of the resultant minimal string on a new line.


def stringReduction(s):
    count = len(s)
    count_dict = {"a": 0, "b": 0, "c": 0}

    for i in range(count):
        count_dict[s[i]] += 1
    
    if (count_dict["a"] == count or count_dict["b"] == count or count_dict["c"] == count):
        return count
    elif ((count_dict["a"] % 2 == 0 and count_dict["b"] % 2 == 0 and count_dict["c"] % 2 == 0) or (count_dict["a"] % 2 == 1 and count_dict["b"] % 2 == 1 and count_dict["c"] % 2 == 1)):
        return 2
    else:
        return 1
    
