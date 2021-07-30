def meuGrep(filename, word):

    infile = open(filename, 'r')
    lines = infile.readlines()
    infile.close()

    #print(lines)

    #print(len(lines[1]))

    for i in range(len(lines)):

        if len(lines[i]) > 1:
            print('yes')
            counter = 0
            wordList = lines[i].split()

            for step in wordList:
                if step == word:
                    counter += 1
            if counter > 1:
                print(lines[i])

        else:
            print('no')

    '''
    
    counter = 0

    for i in range(len(lines)):

        wordList = lines[i].split()

        if len(wordList) > 1:

            for step in wordList:
                if step == word:
                    counter += 1

            if counter > 0:
                print(lines[i])
                counter = 0
                
'''
    #for line in lines:

    # counter = 0

    # divide = line.split()

    # for step in divide:
    #if step == word:
    #counter += 1

    #if counter > 0:

    # print(line, end='')

meuGrep('teste.txt', 'line')