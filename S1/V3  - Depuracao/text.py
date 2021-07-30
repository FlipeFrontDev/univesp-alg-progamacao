def numLines(nomearq):
    'Retorno o número de linhas de nomearq'
    arqentrada = open(nomearq, 'r')
    listalinhas = arqentrada.readlines()
    arqentrada.close()

    print(listalinhas)
    return len(listalinhas)