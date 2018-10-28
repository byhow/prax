#
# Complete the 'getMaxOccurrences' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER minLength
#  3. INTEGER maxLength
#  4. INTEGER maxUnique
#

def getMaxOccurrences(s, minLength, maxLength, maxUnique):
    # Write your code here
    occr = dict()
    max_occr = 1
    l = len(s)

    for i in range(l):
        j = minLength

        while j <= maxLength and i + j <= l:
            substring = s[i:(j + i)]
            len_char = len(set(substring))
            # print("substring is " + substring)
            if len_char > maxUnique:
                pass
            else:
                if substring in occr:
                    occr[substring] += 1
                    if occr[substring] > max_occr:
                        max_occr = occr[substring]
                        # print(occr)
                else:
                    occr[substring] = 1
            j += 1
        
    # print(occr)
    return max_occr



print(getMaxOccurrences("abababab", 2, 4, 5))