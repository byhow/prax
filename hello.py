# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    row = 0
    max_height = A[0]
    local_l = []
    
    for i in A:
        local_l.append(i)
                
        if i >= max_height:
            max_height = i
            row += 1
        
        elif i > min(local_l):
            row += 1
            max_height = i
     
    return row