import time

m = dict()

def fat(n):
    if n == 0:
        return 1
    elif m.get(n) != None:
        return m[n]
    else:
        m[n] = n * fat(n-1)
        return m[n]

n = 20

startTime = time.time()
print(fat(n))

period = float(time.time() - startTime)

print('Memoization: %.18f ' % (period))