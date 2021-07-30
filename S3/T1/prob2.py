def cheers(n):

    if n == 0:
        print('Hurrah!!!')
    else:
        print('Hip', end=' ')
        cheers(n-1)