def meuGrep(filename, word):

    infile = open(filename, 'r')
    lines = infile.readlines()
    infile.close()

    for line in lines:

        counter = 0

        if (len(line)) > 1:

            wordlist = line.split()

            for step in wordlist:

                if step == word:
                    counter += 1
                    print(line, end='')

meuGrep('teste.txt', 'line')