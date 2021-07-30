class Point:
    'Inicia objeto no momento da instanciação'
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    'Define a coordenada x de ponto'
    def setx(self, x):
        self.x = x
    'Define a coordenada y de ponto'
    def sety(self, y):
        self.y = y
    'Retorna as coordenadas x e y de ponto como uma tupla (x, y)'
    'Tupla: tipo de lita que armazena tipos diferentes de dados em mesmo registro'
    def get(self):
        return self.x, self.y
    'Altera as coordenadas do ponto de (x, y) atual para(x+offsetx, y+offsety)'
    def move(self, offsetx, offsety):
        self.x += offsetx
        self.y += offsety

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __add__(self, other):
        if type(other) == Point:
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other, self.y + other)

    def __sub__(self, other):
        if type(other) == Point:
            return Point(self.x - other.x, self.y - other.y)
        else:
            return Point(self.x - other, self.y - other)

    def __mul__(self, other):
        if type(other) == Point:
            return Point(self.x * other.x, self.y * other.y)
        else:
            return Point(self.x * other, self.y * other)

    def __truediv__(self, other):
        if type(other) == Point:
            return Point(self.x / other.x, self.y / other.y)
        else:
            return Point(self.x / other, self.y / other)

    def __floordiv__(self, other):
        if type(other) == Point:
            return Point(self.x // other.x, self.y // other.y)
        else:
            return Point(self.x // other, self.y // other)

    def __mod__(self, other):
        if type(other) == Point:
            return Point(self.x % other.x, self.y % other.y)
        else:
            return Point(self.x % other, self.y % other)

    def __eq__(self, other):
        if type(other) == Point:
            return Point(self.x == other.x, self.y == other.y)
        else:
            return Point(self.x == other, self.y == other)

    def __ne__(self, other):
        if type(other) == Point:
            return Point(self.x != other.x, self.y != other.y)
        else:
            return Point(self.x != other, self.y != other)

    '''
    Pesquisar
    
    def __len__(self, other):
        return Point(len(other.x), len(other.y))
    
    '''

