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

def shift_table(P, sigma):
    m = len(P)
    size = len(sigma)
    table = list(range(size))
    sigma_dict = compute_dict(sigma)

    for i in range(size):
        table[i] = m
    for i in range(m-1):
        c = sigma_dict[P[i]]
        table[c] = m-1-i
    return table

def horspool_matching(P, T, sigma):
    tbl = shift_table(P, sigma)
    sigma_dict = compute_dict(sigma)
    m = len(P)
    n = len(T)
    size = len(sigma)
    
    i = m-1
    while i < n:
        k = 0
        while k < m and P[m-1-k] == T[i-k]:
            k = k + 1
        if k == m:
            return i-m+1
        else:
            c = sigma_dict[T[i]]
            i = i + tbl[c]
    return -1

T = "jim_saw_me_in_a_barbershop"
P = "barber"
sigma = compute_sigma(T)

s = horspool_matching(P, T, sigma)
print(s)

