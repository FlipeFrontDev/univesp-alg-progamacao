class Horario:

    def __init__(self, h, m, s):
        self.hora = h
        self.minuto = m
        self.segundo = s

    def __repr__(self):

       return str(self.hora) + ':' + str(self.minuto) + ':' + str(self.segundo)