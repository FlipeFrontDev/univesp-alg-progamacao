def stringCout(filename, entering):
    locate = 0

    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    wordlist = content.split()

    print(wordlist)

    for word in wordlist:
        if word == entering:
            locate += 1
        elif word == entering + '.':
            locate += 1

    return(locate)

print(stringCout('teste.txt', 'line'))