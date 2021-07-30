def fatorial(n):

    if n == 0:
        return 1
    else:
        rec = fatorial(n-1)
        return n * rec