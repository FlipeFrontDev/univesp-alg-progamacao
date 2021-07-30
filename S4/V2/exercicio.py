class Fila():

    def __init__(self):

        self.normal = []
        self.prioritaria = []

        self.contador = 0

    def __repr__(self):

        return '(' + str(self.normal) + '\n' + str(self.prioritaria) + ')'

    def inserir(self, idade):

        if idade > 60:

            self.prioritaria.append(idade)

        else:
            self.normal.append(idade)

    def remover(self):

        if len(self.prioritaria) > 0 and self.contador < 2:

            self.contador += 1
            self.prioritaria.pop(0)

        elif len(self.normal) > 0:

            self.normal.pop(0)
            self.contador = 0