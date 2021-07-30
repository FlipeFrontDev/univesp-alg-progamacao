Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> line1 = 'Olá, desenvolvedor Python...'
>>> line2 = 'Bem vindo ao mundo python!'
>>> print(line1)
Olá, desenvolvedor Python...
>>> print(line1)
Olá, desenvolvedor Python...
>>> print(line1 + '\n' + line2)
Olá, desenvolvedor Python...
Bem vindo ao mundo python!
>>> 
================================ RESTART: Shell ================================
>>> print(line1)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(line1)
NameError: name 'line1' is not defined
>>> x = input('Digite seu nome')
Digite seu nome5
>>> x
'5'
>>> 