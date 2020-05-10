def s1(N):
    result = 0
    curr = 0
    binary = "{0:b}".format(N)
    for bit in binary:
        if bit == "0":
            curr += 1
        if bit == "1":
            if curr > result:
                result = curr
                curr = 0
            else:
                curr = 0
    return result