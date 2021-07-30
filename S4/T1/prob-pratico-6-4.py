def contaPalavra(texto):

    palavras = texto.split()

    contadores = {}

    for palavra in palavras:
        if palavra in contadores:
            contadores[palavra] += 1
        else:
            contadores[palavra] = 1

    #return contadores

    for palavra in contadores:

        if contadores[palavra] == 1:
            print('{:8} aparece {} vez.'.format(palavra, contadores[palavra]))
        else:
            print('{:8} aparece {} vezes.'.format(palavra, contadores[palavra]))

texto = 'all animals are equal but some \
animals are more equal than others'