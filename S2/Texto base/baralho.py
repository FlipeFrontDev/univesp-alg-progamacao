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
        return '(' + self.valor + self.naipe + ')'

class Baralho:

    naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}

    valores = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    def __init__(self, valores = []):

        self.baralho = []

        if valores != []:

            self.valores = valores

            for valor in self.valores:

                self.baralho.append(Carta(valor))

        else:

            for naipe in Baralho.naipes:
                for valor in Baralho.valores:

                    self.baralho.append(Carta(valor, naipe))

    def distribuiCarta(self):
        return self.baralho.pop()

    def shuffle(self):
        shuffle(self.baralho)