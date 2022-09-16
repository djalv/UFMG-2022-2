import numpy as np

def compute_prefix_function(P):
    m = len(P)
    p = np.zeros(m)
    p[0] = 0
    k = 0
    for q in range(1,m):
        while k > 0 and P[k] != P[q]:
            k = int(p[k])
        if P[k] == P[q]:
            k = k + 1
        p[q] = k
    return p

def KMP_matcher(P,T):
    n = len(T)
    m = len(P)
    p = compute_prefix_function(P)
    q = 0
    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = int(p[q])
        if P[q] == T[i]:
            q = q + 1
        if q == m:
            print("Padrão ocorre com deslocamento ", i-m+1)
            q = int(p[q-1])

T = "ABCD"
P = "CDAB"
print(compute_prefix_function(P))
KMP_matcher(P, T)
