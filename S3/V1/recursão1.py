def imprime_rec(l, i=0):
    if i < len(l):
        print(str(l[i]) + '\n')
        imprime_rec(l, i+1)