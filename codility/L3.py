def s4(X, Y, D):
    way = Y-X
    if way % D == 0:
        return way//D
    else:
        return way//D + 1

def s5(A):
    temp = 1
    A.sort()
    for i in range(len(A)):
        if A[i] == temp:
            temp += 1
        else:
            return temp
    return temp

def s6(A):
    n = len(A)
    mini = 1000000 #maxint
    curr = A[0]
    total = sum(A) - curr
    for i in range(1, n):
        difference = abs(curr - total)
        total -= A[i]
        curr += A[i]
        if difference < mini:
            mini = difference
    return mini
