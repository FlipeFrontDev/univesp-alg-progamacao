class EmptyQueueError(Exception):

    pass

class fruta():

    def __init__(self):
        'Instancia uma lista que conterá os itens da fila'

        self.q = []

    def __getitem__(self, index):

        return self.q[index]

    def __len__(self):

        return len(self.q)

    def isEmpty(self):
        'Retorna True se a fila estiver vazia, False caso contrário'

        return (len(self.q) == 0)

    def enqueue(self, item):
        'Insere item no final da fila'

        return self.q.append(item)

    def dequeue(self):
        'Remove e retorna um item do inicio da lista'

        if len(self.q) == 0:

            raise EmptyQueueError('Esta fila está vazia!')

        return self.q.pop(0)

    def relatorio(self):

        for item in self.q:
            print(item)


    def relatoriob(self):

        for i in range(len(self.q)):

            print(i)