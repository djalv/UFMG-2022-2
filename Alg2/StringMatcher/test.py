def longest_sufix(P, T):
    n = len(T)
    p = [0] * n
    k = 0

    for q in range(0, n):
        while k > 0 and P[k] != T[q]:
            k = p[k]
        if P[k] == T[q]:
            k = k + 1
        p[q] = k
    return p[-1]

P = "CDAB"
T = "ABCD"

print(longest_sufix(P, T))
