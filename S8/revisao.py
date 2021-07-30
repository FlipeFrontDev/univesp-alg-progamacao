def soma(v,i):
    if i == 0:
        return v[0]
    else:
        return v[i] + soma(v, i-1)

l = [2,3,2]

print(soma(l, len(l)-1))