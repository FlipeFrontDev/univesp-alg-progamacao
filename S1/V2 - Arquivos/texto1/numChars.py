def numChars(filename):
    'Retorna o número de caracteres no arquivo filename'
    arqEntrada = open(filename,'r')
    conteúdo = arqEntrada.read()
    arqEntrada.close()

    return len(conteúdo)

print(numChars('teste.txt'))