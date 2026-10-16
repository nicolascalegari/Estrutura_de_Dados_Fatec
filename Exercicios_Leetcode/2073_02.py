class Fila:
    def __init__(self,capacidade = 100):
        self._capacidade = capacidade
        self._elementos = [None]*self._capacidade
        self._inicio = 0
        self._fim = 0
        self._tamanho = 0


    def empilhar(self,item):
        if self._tamanho == self._capacidade:
            raise OverflowError("Queue Overflow!")

        self._elementos[self._fim] = item

        #logica do circular
        if self._fim+1 >= self._capacidade:
            self._fim = 0
        else:
            self._fim += 1

        self._tamanho += 1

    def desempilhar(self):
        if self.eh_vazio():
            raise IndexError("Queue Underflow!")

        item = self._elementos[self._inicio]

        #logica do circular
        if self._inicio+1 >= self._capacidade:
            self._inicio = 0
        else:
            self._inicio += 1

        self._tamanho -= 1

        return item

    def topo(self):
        if self.eh_vazio():
            raise IndexError("Queue Underflow!")

        item = self._elementos[self._inicio]

        return item

    def eh_vazio(self):
        return self._tamanho == 0

    def tamanho(self):
        return self._tamanho

#___________________________________________________________________

class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:

        # Criar a fila com capidade suficiente
        fila = Fila(capacidade=len(tickets) + 1)

        # Enfileira usando enumarate 
        # guarda indice e ingressos
        for i, ingressos in enumerate(tickets):
            fila.empilhar((i, ingressos))

        tempo_total = 0

        # Rodar fila
        while not fila.eh_vazio():

            # Remove a pessoa da frente da fila
            pessoa_atual, ingressos_res = fila.desempilhar()

            # Compra um ingresso e o tempo passa
            ingressos_res -= 1
            tempo_total += 1

            # se for a pessoa K e ela chegou a 0 ingressos, paramaos o tempo
            if pessoa_atual == k and ingressos_res == 0:
                return tempo_total

            # Se ela inda precisar de mais ingressos, volta para o fim da dila
            if ingressos_res > 0:
                fila.empilhar((pessoa_atual, ingressos_res))

        return tempo_total