class Vetor():

    def __init__(self, x = '', y = ''):

        self.x = x
        self.y = y

    def __add__(self, other):

        if type(other) == Vetor:

            return Vetor(self.x + other.x, self.y + other.y)

    def __mul__(self, other):

        if type(other) == Vetor:

            return (self.x * other.x + self.y * other.y)

    def __repr__(self):

        return '(' + str(self.x) + ', ' + str(self.y) + ')'