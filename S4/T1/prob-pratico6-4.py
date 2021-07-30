def contaPalavra(texto):

    listaPalavras = texto.split()

    lista ={}

    for palavra in listaPalavras:
        if palavra in lista:
            lista[palavra] += 1
        else:
            lista[palavra] = 1

    for palavra in lista:

        if lista[palavra] == 1:
            print('{:8} aparece {} vez.'.format(palavra, lista[palavra]))
        else:
            print('{:8} aparece {} vezes.'.format(palavra, lista[palavra]))

texto = 'all animals are equal but some \
animals are more equal than others'