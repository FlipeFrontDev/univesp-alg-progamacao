class Animal:
    'Representa um animal'

    def __init__(self, espécie = '', linguagem = ''):
        self.espécie = espécie
        self.linguagem = linguagem

    '''
    def setEspécie(self, espécie):
        'Define a espécie do animal'
        self.espécie = espécie

    def setLinguagem(self, linguagem):
        'Define a linguagem do animal'
        self.linguagem = linguagem
    '''

    def fala(self):

        'Exibe a sentença possível de ser criada pelo animal'

        if (self.espécie !='' and self.linguagem ==''):

            print('Eu sou {} e eu sei emitir sons.'.format(self.espécie))

        elif (self.espécie =='' and self.linguagem !=''):

            print('Eu sou um animal e eu sei {}.'.format(self.linguagem))

        elif (self.espécie !='' and self.linguagem !=''):

            print('Eu sou um {} e eu sei {}.'.format(self.espécie, self.linguagem))

        else:

            print('Eu sou animal e eu sei emitir sons')