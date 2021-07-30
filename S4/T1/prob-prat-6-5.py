agenda = {('Anna', 'Karenina'): '(123)456-78-90',
          ('Yu', 'Tsun'): '(901)234-56-78',
          ('Hans', 'Castorp'): '(321)908-76-54'}

def lookup(agenda):

    while True:

        nome = input('Digite o nome: ')
        sobrenome = input('Digite o sobrenome: ')

        pessoa = (nome, sobrenome)

        if pessoa in agenda:

            print(agenda[pessoa])

        else:

            print('Registro inexistente!')