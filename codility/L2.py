def s2(A, K):

    def one_rotation(tab):
        n = len(tab)
        temp = tab[n-1]
        for i in range(n-1, -1, -1):
            tab[i] = tab[i-1]
        tab[0] = temp

    for i in range(K):
        one_rotation(A)
        
    return A


def s3(A):
    result = A[0]
    for i in range(1, len(A)):
        result ^= A[i]
    return result