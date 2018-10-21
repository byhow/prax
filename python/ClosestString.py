# #
# # Complete the 'closest' function below.
# #
# # The function is expected to return an INTEGER_ARRAY.
# # The function accepts following parameters:
# #  1. STRING s
# #  2. INTEGER_ARRAY queries
# #

# def closest(s, queries):
#     # Write your code here

#     ind_arr = []
#     occu = dict()

#     for i in range(len(s)):
#         if s[i] in occu:
#             occu[s[i]].append(i)
#         else:
#             occu[s[i]] = [i]
   
#     for i in queries:
#         min_dist = len(s)
#         found = True
#         for j in occu[s[i]]:
#             if len(occu[s[i]]) == 1:
#                 ind_arr.append(-1)
#                 found = False
#                 break
#             elif j != i:
#                 if abs(j - i) < min_dist:
#                     min_dist = abs(j - i)
#         if found == True:
#             if s[i - min_dist] == s[i] and i - min_dist != -1:
#                 ind_arr.append(i - min_dist)
#             elif s[i + min_dist] == s[i]:
#                 ind_arr.append(i + min_dist)
        
    
#     print(occu)

#     return ind_arr

# print(closest("aaaa", [0, 1, 2, 3]))



#
# Complete the 'closest' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def closest(s, queries):
    # Write your code here

    ind_arr = []
    min_ind = 0
    max_ind = len(s)

    for j in queries:
        found_min = False
        found_max = False
        needle = s[j]
        min_ind = 0
        max_ind = len(s)
        k = j + 1
        while k < max_ind:
            current_chr = s[k]
            # print(current_chr)
            if s[k] == needle:
                max_ind = k
                found_max = True
                break
            k += 1
        
        k = j - 1
        while k >= min_ind:
            if s[k] == needle:
                min_ind = k
                found_min = True
                break
            k -= 1
        
        if found_max and found_min:
            if abs(min_ind - j) > abs(max_ind - j):
                ind_arr.append(max_ind)
            else:
                ind_arr.append(min_ind)
        else:
            if found_max:
                ind_arr.append(max_ind)
            elif found_min:
                ind_arr.append(min_ind)
            else:
                ind_arr.append(-1)

    return ind_arr

print(closest("aaaa", [0, 1, 2, 3]))