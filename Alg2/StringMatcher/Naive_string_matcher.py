def naive_string_matcher(T,P):
    n = len(T)
    m = len(P)

    for s in range(n-m+1):
        temp_text = ""
        
        for i in range(s, s+m):
            temp_text += T[i]
        
        if(P == temp_text):
            print("Padrão ocorre com deslocamento ", s)


T = "Alvaro Candido de Oliveira Neto"
P = "a"

naive_string_matcher(T,P)
