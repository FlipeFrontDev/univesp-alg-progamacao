def ler(filename):
    infile = open('teste.txt', 'r')
    content = infile.read()
    infile.close()
    print(content)