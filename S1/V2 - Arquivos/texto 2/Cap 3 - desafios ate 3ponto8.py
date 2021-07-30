Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> max(4, 7)
7
>>> sum([4, 5, 6, 7])
22
>>> def average(num1, num2):
	result = (num1 + num2) / 2
	print(result)

	
>>> average(10, 10)
10.0
>>> def average():

	num1 = input('Digite o valor 1: ')
	num2 = input('Digite o valor 2: ')

	result = (num1 + num2) / 2
	print(result)

	
>>> average()
Digite o valor 1: 8
Digite o valor 2: 8
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    average()
  File "<pyshell#8>", line 6, in average
    result = (num1 + num2) / 2
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> def average():

	num1 = eval(input('Digite o valor 1: '))
	num2 = eval(input('Digite o valor 2: '))

	result = (num1 + num2) / 2
	print(result)

	
>>> average()
Digite o valor 1: 8
Digite o valor 2: 8
8.0
>>> average()
Digite o valor 1: 2
Digite o valor 2: 3,5
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    average()
  File "<pyshell#11>", line 6, in average
    result = (num1 + num2) / 2
TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
>>> average()
Digite o valor 1: 2
Digite o valor 2: 3.5
2.75
>>> 