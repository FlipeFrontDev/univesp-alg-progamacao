def vertical(num):

    if num < 10:
        print(num)
    else:

        vertical(num // 10)
        print(num % 10)