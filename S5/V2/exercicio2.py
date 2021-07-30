def quick_sort(v,ini,fim):
    meio = (ini + fim) // 2
    pivo = v[meio]

    i = ini
    j = fim

    while i < j:
        while v[i] < pivo:
            i += 1

        while v[j] > pivo:
            j -= 1
        if i <= j:
            v[i], v[j] = v[j], v[i]
        i += 1
        j -= 1
    if j > ini:
        quick_sort(v, ini, j)
    if i < fim:
        quick_sort(v,i,fim)

    return v

v = [22,33,35,12,37,86,92,57]

ini = 0

fim = len(v)-1