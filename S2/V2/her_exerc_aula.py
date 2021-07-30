class Funcionario:
    def __init__(self, nome = '', dt_admiss = '', salario = 0):
        self.nome = nome
        self. dt_admiss = dt_admiss
        self.salario = 0

        # if type(self) == Gerente:
        #
        #     self.salario = (salario * 1.25)
        #
        # else:
        #
        #     self.salario = salario

    def setnome(self, nome):
        self.nome = nome

    def setdt_admiss(self, dt_admiss):
        self.dt_admiss = dt_admiss

    def setsalario(self, salario):

            self.salario = salario

    def get(self):
        return self.nome, self.dt_admiss, self.salario

    def __repr__(self):
        return '(' + self.nome + ', ' + self.dt_admiss + ', ' + str(self.salario) + ')'

class Gerente(Funcionario):

    def setsalario(self, sal):

        self.salario = (sal * 1.25)