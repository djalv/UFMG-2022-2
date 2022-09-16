import numpy as np

def compute_sigma(T): # O(n^2)
    sigma = []
    for a in T:
        if a not in sigma:
            sigma.append(a)
    return sigma

def compute_dict(sigma): # O(|sigma|)
    sigma_dict = {}
    i = 0
    for a in sigma:
        sigma_dict[a] = i
        i = i + 1
    return sigma_dict

def get_prefix(P, k): # O(m)
    st = ""
    for i in range(k):
        st += P[i]
    return st

def is_sufix(P, T): # O(m)
    m = len(P)
    n = len(T)

    if m > n:
        return False
    elif m == n:
        if P == T:
            return True
    for i in range(m):
        if(m+i-1 >= n):
            return False
        else:
            if P[i] != T[n-m+i]:
                return False
    return True

def compute_transition_function(P, sigma): # O((m^3)|sigma|)
    m = len(P)
    delta = np.zeros((m+1, len(sigma)))
    sigma_dict = compute_dict(sigma)

    for q in range(m+1):
        for a in sigma:
            k = min(m+1, q+2)
            while True:
                k = k - 1
                Pk = get_prefix(P, k) #O(m)
                Pqa = get_prefix(P, q) #O(m)
                Pqa += a
                if(is_sufix(Pk,Pqa)):
                    break
            delta[q][sigma_dict[a]] = k
    return delta

def finite_automata_matcher(T, delta, sigma, m): # O(n)
    n = len(T)
    q = 0
    sigma_dict = {}
    sigma_dict = compute_dict(sigma)
    
    for i in range(n):
        q = int(delta[q][sigma_dict[T[i]]])
        if q == m:
            print ("Padrão Ocorre com deslocamento ", i-m+1)

T = "abbababaca"
P = "ababaca"
sigma = compute_sigma(T)

delta = compute_transition_function(P, sigma)
finite_automata_matcher(T, delta, sigma, len(P))

print(delta)
