import math

def s1(X):
    result = []
    for i in range(2, X + 1):
        result.append(i)
    i = 2
    while(i <= (int(math.sqrt(X)))):
        if i in result:
            for j in range(i*2, X + 1, i):
                if j in result:
                    result.remove(j)
        i += 1
    return result


def solution(S):
    tab = list(S)
    if len(tab)%2 == 0:
        half = len(tab)//2
        for i in range(half - 1, -1, -1):
            first = len(tab) -1 - i
            sec = i
            if tab[first] == tab[sec]:
                continue
            elif tab[first] == "?" and tab[sec] == "?":
                tab[first] = "a"
                tab[sec] = "a"
            elif tab[first] == "?" and tab[sec] != "?":
                tab[first] = tab[sec]
            elif tab[first] != "?" and tab[sec] == "?":
                tab[sec] = tab[first]
            elif tab[first] != tab[sec]:
                return -1
    elif len(tab)%2 == 1:
        half = len(tab)//2
        if tab[half] == "?":
            tab[half] = "a"
        for i in range(half - 1, -1, -1):
            first = len(tab) -1 - i
            sec = i
            if tab[first] == tab[sec]:
                continue
            elif tab[first] == "?" and tab[sec] == "?":
                tab[first] = "a"
                tab[sec] = "a"
            elif tab[first] == "?" and tab[sec] != "?":
                tab[first] = tab[sec]
            elif tab[first] != "?" and tab[sec] == "?":
                tab[sec] = tab[first]
            elif tab[first] != tab[sec]:
                return -1
        
    return ''.join(tab)

print(solution("z??bz"))
        
