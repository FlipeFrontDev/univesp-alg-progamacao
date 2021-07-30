def meuGrep(filename, word):

    infile = open(filename, 'r')
    lines = infile.readlines()
    infile.close()



    for i in range(len(lines)):

        if len(lines[i]) > 1:

            counter = 0

            wordlist = lines[i].split()

            for step in wordlist:
                if step == word:
                    counter += 1

            if counter > 0:
                print(lines[i])

        else:
            print('no')

meuGrep('teste.txt', 'line')
