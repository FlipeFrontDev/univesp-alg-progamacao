def fatorial(n):
    if n == 0:
        return 1
    else:
        fat = n * fatorial(n - 1)
        return fat