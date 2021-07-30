arqSaida = open('teste2.txt', 'w')

arqSaida.write('Esta é a primeira linha.')
arqSaida.write('Ainda a primeira linha. \n')
arqSaida.write('Agora estamos na segunda linha\n')
arqSaida.write('Valor não de string como '+str(5)+' deve ser convertido primeiro.\n')
arqSaida.write('Valor não de string como {} deve ser convertido primeiro.\n'.format(5))

arqSaida.close()