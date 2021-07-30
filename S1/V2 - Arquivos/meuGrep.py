def meuGrep(filename, word):

    infile = open(filename, 'r')
    lines = infile.readlines()

    for i in range(1, len(lines)):

        line = infile.readline(i)
        words = line.split()

        counter = 0

        for step in words:

            if step == word:

                counter += 1

        if counter > 0:
            print(line)

    infile.close()

meuGrep('teste.txt', 'line')