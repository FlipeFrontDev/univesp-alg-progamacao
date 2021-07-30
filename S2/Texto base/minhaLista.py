import random

class MinhaLista():

    def __init__(self, inicial = []):

        self.lst = inicial

    def __len__(self):
        return len(self.lst)

    def append(self, item):
        self.lst.append(self, item)

    def escolha(self):

        return random.escolha(self.lst)