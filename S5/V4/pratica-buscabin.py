def buscabin(l, x, inicio, fim):

    meio = (inicio + fim ) // 2

    if x == l[meio]:
        return meio

    if x < l[meio]:
        return buscabin(l, x, inicio, meio-1)

    if x > l[meio]:
        return buscabin(l, x, meio+1, fim)