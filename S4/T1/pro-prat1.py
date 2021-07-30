estado = {'Barack Hussein Obama II': 'Hawaii',

          'George Walker Bush': 'Connecticut',

          'William Jefferson Clinton': 'Arkansas',

          'George Herbert Walker Bush': 'Massachussetts',

          'Ronald Wilson Reagan': 'Illinois',

          'James Earl Carter, Jr': 'Georgia'}

def estudoNasc():

    nome = input('Didite o nome de algum presidente dos EUA: ')

    if nome == '':

        print('Digite um nome válido!')

    return 'Este presidente nasceu em ' + estado[nome]