class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def pegaValor(self):
        return self.valor

    def pegaNaipe(self):
        return self.naipe

    def __repr__(self):
        return '(' + self.valor + self.naipe + ')'