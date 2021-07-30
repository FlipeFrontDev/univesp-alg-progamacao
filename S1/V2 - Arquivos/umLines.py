def numLines(filename):
    infile = open(filename, 'r')
    linesList = infile.readlines()
    infile.close()

    print(linesList)

    return len(linesList)

numLines('teste.txt')