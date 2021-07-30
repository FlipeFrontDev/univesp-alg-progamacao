#tipos mutaveis e imutaveis (p. 76)

a = 3
b = a

print(a)
print(b)

a = 6

print(a)
print(b)

print('\n')

c = [3,4,5]
d = c

c[1] = 8

print(c)
print(d)


e = [5,6,7]
f = e
e = 3

print(e)
print(f)