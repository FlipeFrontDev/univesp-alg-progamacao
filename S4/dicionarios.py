def frequência(listaItens):

    contadores = {}

    for item in listaItens:
        if item in listaItens:
            contadores[item] += 1
        else:
            contadores[item] = 1

    return contadores