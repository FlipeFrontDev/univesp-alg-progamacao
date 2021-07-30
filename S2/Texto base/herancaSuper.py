class Super():
    'Classe genérica com um método'

    def método(self):
        print('em super.método')

class Herdeiro(Super):
    'Herda métodos da classe super'

    pass

class Substituto(Super):
    'Classe que redefine o método'

    def método(self):

        print('em Substituto.método')

class Extensor(Super):
    'Herda atribs. da classe super e subs. métodos de mesmo nome'

    def método(self):

        print('Iniciando Extensor.método')

        Super.método(self)

        print('Finalizando Extensor.método')