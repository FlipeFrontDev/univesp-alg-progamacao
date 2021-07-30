Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: C:/Univesp/Alg prog 2/texto 2/iteracoes-1.py ============
>>> word = input('Digite uma palavra: ')
Digite uma palavra: eat
>>> for char in word:
	print(char)

	
e
a
t
>>> animals = ['peixe', 'gato', 'cão']
>>> for animal in animals:
	print(animal)

	
peixe
gato
cão
>>> #Desario pratico 3.5
>>> lista[] = input('Digite a lista de palavras: ')
SyntaxError: invalid syntax
>>> lista = []
>>> lista = [4]
>>> print(lista)
[4]
>>> lista = []
>>> for i in range(4):
	lista.append(input('Digite uma palavra: '))

	
Digite uma palavra: Amor
Digite uma palavra: Amora
Digite uma palavra: Laranja
Digite uma palavra: pessego
>>> def list():
	lista = []

	qtde = input('Quantas palavras deseja comparar? ')
	
	for i in qtde:
		lista.append(input('Digite uma palavra: '))
	for word in lista:
		if len(word) == 4:
			print(word + '\n')

			
>>> list()
Quantas palavras deseja comparar? 4
Digite uma palavra: pare
pare

>>> def list():
	lista = []

	qtde = input('Quantas palavras deseja comparar? ')
	
	for i in qtde:
		lista.append(input('Digite uma palavra: '))

		
>>> def list():
	lista = []

	qtde = eval(input('Quantas palavras deseja comparar? '))
	
	for i in qtde:
		lista.append(input('Digite uma palavra: '))
	for word in lista:
		if len(word) == 4:
			print(word + '\n')

			
>>> list()
Quantas palavras deseja comparar? 4
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    list()
  File "<pyshell#31>", line 6, in list
    for i in qtde:
TypeError: 'int' object is not iterable
>>> def list():
	lista = []

	qtde = eval(input('Quantas palavras deseja comparar? '))
	
	for i in range(qtde):
		lista.append(input('Digite uma palavra: '))
	for word in lista:
		if len(word) == 4:
			print(word + '\n')

			
>>> list()
Quantas palavras deseja comparar? 4
Digite uma palavra: pare
Digite uma palavra: desktop
Digite uma palavra: tio
Digite uma palavra: pote
pare

pote

>>> for i in range(2, 5):
	print(i)

	
2
3
4
>>> for i in range(1, 14, 3):
	print(i)

	
1
4
7
10
13
>>> for i in range(1, 20, 5):
	print(i)

	
1
6
11
16
>>> for i in range(3, 12 + 1):
	print(i)

	
3
4
5
6
7
8
9
10
11
12
>>> for i in range(0, 9, 2):
	print(i)

	
0
2
4
6
8
>>> for i in range(0, 24, 3)
SyntaxError: invalid syntax
>>> for i in range(0, 24, 3):
	print(i)

	
0
3
6
9
12
15
18
21
>>> for i in range(3, 12, 5):
	print(i)

	
3
8
>>> exit()
>>> 