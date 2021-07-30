class Retângulo:

    def __init__(self, largura, comprimento):
        self.largura = largura
        self.comprimento = comprimento

    def setTamanho(self, largura, comprimento):
            self.largura = largura
            self.comprimento = comprimento

    def perimetro(self):
        return (self.largura + self.comprimento) * 2

    def área(self):
        return (self.largura * self.comprimento)