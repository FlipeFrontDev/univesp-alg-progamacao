Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def imc(peso, altura):
	'Cálcula o IMC de uma pessoa.'
	resultado = peso * (altura * altura)
	return(resultado)
def indice(nome, idade):
	
SyntaxError: invalid syntax
>>> def indice(nome, idade, pesob, alturab):
	imc(pesob, alturab)

	
>>> def indice(nome, idade, pesob, alturab):
	imc(pesob, alturab)

	
>>> def indice(nome, idade, pesob, alturab):
	'Defini a status de saúde de uma pessoa'
	massa = imc(pesob, alturab)
	if idade >= 16 and idade <= 17 and massa > 24,45:
		
SyntaxError: invalid syntax
>>> def indice(nome, idade, pesob, alturab):
	'Defini a status de saúde de uma pessoa'
	massa = imc(pesob, alturab)
	if idade >= 16 and idade <= 17 and massa > 24,45:
		
SyntaxError: invalid syntax
>>> def indice(nome, idade, pesob, alturab):
	'Defini a status de saúde de uma pessoa'
	massa = imc(pesob, alturab)
	if idade >= 16 and idade <= 17 and massa > 24,45:
		
SyntaxError: invalid syntax
>>> def indice(nome, idade, pesob, alturab):
	'Defini a status de saúde de uma pessoa'
	massa = imc(pesob, alturab)
	print('Olá ' +nome+ '\n. Você tem ' + idade + ' anos eseu IMC é: ' + massa)

	
>>> def indice(nome, idade, pesob, alturab):
	'Defini a status de saúde de uma pessoa'
	massa = imc(eval(pesob), eval(alturab))
	print('Olá ' +nome+ '\n. Você tem ' + idade + ' anos eseu IMC é: ' + massa)

	
>>> def imc(eval(peso, eval(altura)):
	'Cálcula o IMC de uma pessoa.'
	resultado = peso * (altura * altura)
	return(resultado)
	
SyntaxError: invalid syntax
>>> def imc(eval(peso), eval(altura)):
	'Cálcula o IMC de uma pessoa.'
	resultado = peso * (altura * altura)
	return(resultado)
SyntaxError: invalid syntax
>>> def imc(peso, altura):
	'Cálcula o IMC de uma pessoa.'
	resultado = eval(peso) * (eval(altura) * eval(altura))
	return(resultado)

>>> def indice(nome, idade, pesob, alturab):
	'Defini a status de saúde de uma pessoa'
	massa = imc(pesob, alturab)
	print('Olá ' +nome+ '\n. Você tem ' + idade + ' anos eseu IMC é: ' + massa)

	
>>> indice('Felipe', '30', '75', '1.80')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    indice('Felipe', '30', '75', '1.80')
  File "<pyshell#23>", line 4, in indice
    print('Olá ' +nome+ '\n. Você tem ' + idade + ' anos eseu IMC é: ' + massa)
TypeError: can only concatenate str (not "float") to str
>>> def indice(nome, idade, pesob, alturab):
	'Defini a status de saúde de uma pessoa'
	massa = imc(pesob, alturab)
	print('Olá ' +str(nome)+ '\n. Você tem ' +str(idade)+ ' anos eseu IMC é: ' +str(massa))

	
>>> indice('Felipe', '30', '75', '1.80')
Olá Felipe
. Você tem 30 anos eseu IMC é: 243.00000000000003
>>> def imc(peso, altura):
	'Cálcula o IMC de uma pessoa.'
	resultado = eval(peso) / (eval(altura) * eval(altura))
	return(resultado)

>>> indice('Felipe', '30', '75', '1.80')
Olá Felipe
. Você tem 30 anos eseu IMC é: 23.148148148148145
>>> help(indice)
Help on function indice in module __main__:

indice(nome, idade, pesob, alturab)
    Defini a status de saúde de uma pessoa

>>> help(imc)
Help on function imc in module __main__:

imc(peso, altura)
    Cálcula o IMC de uma pessoa.

>>> round(4.89)
5
>>> s = concat('Bom', 'Dia')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s = concat('Bom', 'Dia')
NameError: name 'concat' is not defined
>>> s = copy('Turbo Pascal', 7, 6)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s = copy('Turbo Pascal', 7, 6)
NameError: name 'copy' is not defined
>>> pos('Pascal', 'Turbo Pascal')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    pos('Pascal', 'Turbo Pascal')
NameError: name 'pos' is not defined
>>> exit()
>>> 