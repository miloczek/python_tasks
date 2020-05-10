def s7(X, A):
    frog = 0
    leaves = [0] * X
    for i in range(len(A)):
        if A[i] <= X:
            leaves[A[i] - 1] = 1
        while leaves[frog]:
            frog += 1
            if frog == X:
                return i
    return -1

def s8(N, A):
    counters = [0] * N
    max_counter = 0
    curr_max = 0
    for instruction in A:
        if instruction == N+1:
            max_counter = curr_max
        else:
            if max_counter > counters[instruction - 1]:
                counters[instruction - 1] = max_counter
            counters[instruction - 1] += 1
            if curr_max < counters[instruction - 1]:
                curr_max = counters[instruction - 1]
    for i in range(N):
        if counters[i] < max_counter:
            counters[i] = max_counter
    return counters

def s9(A):
    if max(A) <= 0:
        return 1
    help_tab = [0] * (len(A) + 1)
    for num in A:
        if num >= 1 and num <= (len(A) + 1):
            help_tab[num-1] = 1
    for i in range(len(A) + 1):
        if help_tab[i] == 0:
            return i + 1