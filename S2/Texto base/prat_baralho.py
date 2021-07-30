from random import shuffle

class Carta:

    def __init__(self, valor ='', naipe =''):
        self.valor = valor
        self.naipe = naipe

    def pegaValor(self):
        return self.valor

    def pegaNaipe(self):
        return self.naipe

    def __repr__(self):
        return "Carta('{}', '{}')".format(self.valor, self.naipe)

    def __eq__(self, outro):
        'self == outro quando eles têm as mesmas coordenadas'

        return self.valor == outro.valor and self.naipe == outro.naipe

class Baralho:

    naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}

    valores = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}

    def __init__(self, outro=''):

        self.baralho = []

        for naipe in Baralho.naipes:
            for valor in Baralho.valores:

                self.baralho.append(Carta(valor, naipe))

    def __repr__(self):
        return 'Baralho ({})'.format(self.baralho)

    def __eq__(self, outro):
        return self.baralho == outro.baralho

    def __len__(self):
        return len(self.baralho)

    def distribuiCarta(self):
        return self.baralho.pop()

    def shuffle(self):
        shuffle(self.baralho)