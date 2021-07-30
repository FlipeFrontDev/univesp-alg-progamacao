#Subst de valores com instrução de atrib multipla

time = ['Ava', 'Eleanor', 'Claire', 'Sarah','Felipe','Andy']

index = len(time)

time[(index - index)], time[index-1] = time[index-1], time[(index - index)]

print(time)