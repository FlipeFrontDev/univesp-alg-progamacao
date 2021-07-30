import random

class MinhaLista():

    def __init__(self, inicial = []):

        'Inicia a lista conforme argumento de entrada'

        self.lst = inicial

    def __len__(self):

        'Retorna quantidade de itens da lista'

        return len(self.lst)

    def append(self, item):

        'Inclui item na lista'

        self.lst.append(self, item)

    def escolha(self):

        'Sorteia um item da lista'

        return random.escolha(self.lst)

    def __repr__(self):

        return '(' + str(self.lst) + ')'

class Queue(MinhaLista):

    'Uma classe de fila, subclasse de MinhaLista'

    def isEmpty(self):

        'Retorna true se a fila está vazia'

        return(len(self.lst == 0))

    def append(self, item):

        'Insere um item no final da fila'

        return self.lst.append(item)

    def escolha(self):

        'Remove um item do inicio da fila'

        return self.lst.pop(0)