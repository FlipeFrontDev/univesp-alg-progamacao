def busca_binaria(l, x, ini, fim):
    meio = (ini + fim) // 2

    if fim < ini:
        return -1

    if x == l[meio]:
        return meio

    if x < l[meio]:
        return busca_binaria(l, x, ini, meio - 1)

    if x > l[meio]:
        return  busca_binaria(l, x, meio + 1, fim)