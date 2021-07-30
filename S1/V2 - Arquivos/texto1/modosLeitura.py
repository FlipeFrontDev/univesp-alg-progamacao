def ler(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    print(content)
    return len(content)

text = ler('teste.txt')
