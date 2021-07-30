def meuGrep(filename, word):

    infile = open(filename, 'r')
    lines = infile.readlines()
    infile.close()

    count = len(lines)

    for i in range(count):

        counter = 0

        for line in lines:

            divide = line.split()

            for step in divide:
                if step == word:

                    counter += 1

                    if counter > 0:
                        print(line)

meuGrep('teste.txt', 'line')